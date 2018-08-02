from organizer.forms import Form
import unittest

class TestForm(unittest.TestCase):
    def test_constructor(self):
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
        }

        Form('form1', fields)

        # Check with all initial turned off
        def remove(name):
            for _, val in fields:
                if hasattr(val, name):
                    del (val[name])

        remove('initial')
        Form('form2', fields)

        # Check with all labels turned off
        remove('label')
        Form('form3', fields)

if __name__ == "__main__":
    unittest.main()