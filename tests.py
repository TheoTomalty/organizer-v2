from django.test.utils import setup_test_environment
setup_test_environment()

#Imports for the test run
from django.test import Client
import pytest

class TestClient(object):
    def test_get_index(self):
        c = Client()
        url = '/'
        
        response = c.get(url)
        assert response.content, 'No html in the response of get({0})'.format(url)
        assert response.context['context'], 'Context is not loaded in the response of get({0})'.format(url)
    
    def test_post_signin(self):
        c = Client()
        url = '/'
        
        response_unauth = c.post(url, {'name':'sign_in', 'username':'test', 'password':'pass'})
        assert response_unauth.status_code == 401, 'Should have raised unauthorized response >> response: {0}'.format(response_unauth)
        
        response_invalid = c.post(url, {'name': 'sign_in', 'test':'test'})
        assert response_invalid.status_code == 400, 'Bad form should have given HTTP400 error >> response: {0}'.format(response_invalid)
        
        pytest.raises(NameError, c.post, url, {'name':'test'})