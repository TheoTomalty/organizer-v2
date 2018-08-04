import copy

from django import forms
import json
import re

class NotDjangoField(Exception):
    pass


class InvalidName(Exception):
    pass

class NoType(Exception):
    pass

class TooFewFields(Exception):
    pass

class UnexpectedField(Exception):
    pass

class InconsistentType(Exception):
    pass

class FormMeta(object):
    def __init__(self, fields):
        ''' Creates a class that inherits django forms, and returns an instance. '''
        self.class_dict = {}
        
        for key in fields:
            self.add_field(key, fields[key])
    
    def get_class(self):
        return type('CustomForm', (forms.Form,), dict(self.class_dict))
    
    def add_field(self, name, arg):
        allowed = ('text', 'choice', 'bool', 'date', 'password')

        if 'type' in arg:
            type = arg['type']
            if type in allowed:
                getattr(self, 'create_' + type).__call__(name, arg)
            else:
                raise NotImplementedError('The type {} is not implemented'.format(type))
        else:
            raise NoType('You must specify a type parameter in your description: {}'.format(arg))

    def create_field(self, name, field):
        if isinstance(field, forms.Field):
            if isinstance(name, str):
                self.class_dict[name] = field
            else:
                raise InvalidName("The name of this field is not a string: {}".format(name))
        else:
            raise NotDjangoField("The item passed is not a Django Field: {}".format(field))

    @staticmethod
    def check_args(argument, required, non_essential):
        for name in required:
            if name not in argument:
                raise TooFewFields('Missing field argument {0} in dict: {1}'.format(name, argument))

        for key in non_essential:
            if key in argument:
                if isinstance(argument[key], type(non_essential[key])):
                    continue
                else:
                    raise InconsistentType('The default type {1} of field argument {0} \
                    is inconsistent with the value passed: {2}'.format(key, 
                                                                       type(argument[key]), 
                                                                       argument[key]))
            else:
                argument[key] = non_essential[key]

        for key in argument:
            if (key not in required and key not in non_essential) and key != 'type':
                raise UnexpectedField('Field argument not recognized: {0}'.format(key))

    def create_text(self, name, argument, password=False):
        FormMeta.check_args(argument, (), {'label': name, 'initial': '', 'required': True})

        self.create_field(
            name,
            forms.CharField(
                label=argument['label'],
                initial=argument['initial'],
                required=argument['required'],
                widget=(forms.PasswordInput() if password else None),
            ),
        )
    
    def create_password(self, name, argument):
        self.create_text(name, argument, password=True)

    def create_choice(self, name, argument):
        FormMeta.check_args(argument, ('choices',), {'label': name, 'required': False})

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
    def __init__(self, name, fields):
        self.prototype = FormMeta(fields).get_class()()
        self.name = name
    
    def __getattr__(self, item):
        try:
            return getattr(self.prototype, item)
        except AttributeError:
            return self.prototype.declared_fields[item]
    
    def __getitem__(self, item):
        return self.prototype.declared_fields[item]
    
    @property
    def html(self):
        return re.sub(r'</p>\n<p>', '<br/>', self.as_p())

class FormManager(object):
    def __init__(self, *args):
        for arg in args:
            if isinstance(arg, Form):
                continue
            else:
                raise TypeError("FormManager takes arguments of type Form")
        
        self.forms = args
    
    def __getitem__(self, item):
        for name, form in zip((f.name for f in self.forms), self.forms):
            if name == item:
                return form
    
    @property
    def window_context(self):
        obj = {}
        for form in self.forms:
            obj[form.name] = form.html
        
        return json.dumps(obj)
    
    def post(self, query_dict):
        self[query_dict['name']].post(query_dict)