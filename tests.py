from django import setup
from django.test.utils import setup_test_environment
setup_test_environment()

#Imports for the test run
from django.test import Client

class TestClient(object):
    def test_get_index(self):
        c = Client()
        
        url = '/'
        
        response = c.get(url)
        assert response.content, 'No html in the response of get({0})'.format(url)
        assert response.context['context'], 'Context is not loaded in the response of get({0})'.format(url)