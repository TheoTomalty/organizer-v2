from django import forms
import re

class NoSuchField(Exception):
    def __init__(self, message="The item passed is not a Django Field"):
        super().__init__(self, message)


class InvalidName(Exception):
    def __init__(self, message="The name of this field is not a string"):
        super().__init__(self, message)


class FormMeta(object):
    def __init__(self, name, fields):
        ''' Creates a class that inherits django forms, and returns an instance. '''
        self.class_dict = {}
        
        for key in fields:
            self.add_field(key, fields[key])
    
    def get_class(self):
        return type('CustomForm', (forms.Form,), self.class_dict)
    
    def add_field(self, name, arg):
        allowed = ('text', 'choice', 'bool', 'date')

        if 'type' in arg:
            type = arg['type']
            if type in allowed:
                getattr(self, 'create_' + type).__call__(name, arg)
        else:
            raise Exception('No type parameter for this field.')

    def create_field(self, name, field):
        if isinstance(field, forms.Field):
            if isinstance(name, str):
                self.class_dict[name] = field
            else:
                raise InvalidName()
        else:
            raise NoSuchField()

    @staticmethod
    def check_args(argument, required, non_essential):
        for name in required:
            if name not in argument:
                raise Exception('Missing field argument: {}'.format(name))

        for key in non_essential:
            if key in argument:
                if isinstance(argument[key], type(non_essential[key])):
                    continue
                else:
                    raise Exception('Field argument {0} does not take type: {1}'.format(key, type(argument[key])))
            else:
                argument[key] = non_essential[key]

        for key in argument:
            if (key not in required and key not in non_essential) and key != 'type':
                raise Exception('Field argument not recognized: {}'.format(key))

    def create_text(self, name, argument):
        FormMeta.check_args(argument, (), {'label': name, 'initial': '', 'required': True})

        self.create_field(
            name,
            forms.CharField(label=argument['label'], initial=argument['initial'], required=argument['required']),
        )

    def create_choice(self, name, argument):
        FormMeta.check_args(argument, ('choices'), {'label': name, 'required': False})

        CHOICES = []
        for key in argument['choices']:
            value = argument['choices'][key]
            if isinstance(value, str) and isinstance(key, str):
                CHOICES.append((key, value))
            else:
                raise Exception("Choices must have key:value pairs that are strings")

        self.create_field(
            name,
            forms.ChoiceField(label=argument['label'], choices=CHOICES, required=argument['required']),
        )

    def create_bool(self, name, argument):
        FormMeta.check_args(argument, (), {'label': name, 'initial': False, 'required': False})

        self.create_field(
            name,
            forms.BooleanField(label=argument['label'], initial=argument['initial'], required=argument['required']),
        )

    def create_date(self, name, argument):
        FormMeta.check_args(argument, (), {'label': name, 'required': True})

        self.create_field(
            name,
            forms.CharField(label=argument['label'], required=argument['required']),
        )
    
class Form(object):
    #def __new__(cls, name, fields):
    #    custom_form_class = FormMeta(name, fields).get_class()
    #    return custom_form_class()
    
    def __init__(self, name, fields):
        self.prototype = FormMeta(name, fields).get_class()()

        self.name = name
    
    def __getattr__(self, item):
        return getattr(self.prototype, item)
    
    @property
    def html(self):
        return re.sub(r'</p>\n<p>', '<br/>', self.as_p())