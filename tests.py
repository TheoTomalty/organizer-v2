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
    
    def test_post_signin(self):
        c = Client()
        url = '/'
        
        response = c.post(url, {'name':'sign_in', 'username':'test', 'password':'pass'})
        assert response.status_code == 200, 'The form posted was not valid >> response: {0}'.format(response)
        
        import pytest
        pytest.raises(NameError, c.post, url, {'name':'test'})
        