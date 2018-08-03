from organizer.forms import *
from django.forms import Form as djForm
from django.forms import Field
import re

fields = {
    'text': {
        'type': 'text',
        'label': 'Test',
        'initial': 'This is a test',
    },
    'choice': {
        'type': 'choice',
        'label': 'Choice',
        'choices': {'one': 'One', 'two': 'Two', 'three': 'Three'},
    },
    'bool': {
        'type': 'bool',
        'label': 'Bool',
        'initial': True,
    },
    'date': {
        'type': 'date',
        'label': 'Date',
    },
    'password': {
        'type': 'password',
        'label': 'Pass',
        'initial': 'test again',
    }
}

class TestForm(object):
    def test_constructor(self):
        f = dict(fields)

        Form('form1', f)

        # Check with all initial turned off
        def remove(name):
            for _, val in f.items():
                if hasattr(val, name):
                    del (val[name])

        remove('initial')
        Form('form2', f)

        # Check with all labels turned off
        remove('label')
        Form('form3', f)
    
    def test_getattr(self):
        form = Form('form1', fields)
        assert form.as_p() # django Forms method
        assert isinstance(form.text, Field) # Class instance
    
    def test_html(self):
        html = Form('form1', fields).html
        assert isinstance(html, str)
        
        assert re.match(r'\n', html) is None
        assert re.compile(r'^<p>').match(html)

class TestFormMeta(object):
    def test_class_creation(self):
        fmeta = FormMeta(fields)
        Class = fmeta.get_class()
        
        for key in fields:
            assert Class.declared_fields[key]
        
        obj = Class()
        assert type(obj).__name__ == 'CustomForm'
        assert isinstance(obj, djForm)
        
        for key in fields:
            assert obj[key]

class TestFormManager(object):
    def test_constructor(self):
        l = []
        for key, value in fields.items():
            l.append(Form(key, {key:value}))
        
        form_manager = FormManager(*l)
        assert form_manager['text']
        
        import json
        assert json.loads(form_manager.window_context)