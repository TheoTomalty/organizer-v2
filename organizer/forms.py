from django import forms

class Form(forms.Form):
    def get_fields(self):
        pass

class LogForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password', widget=forms.PasswordInput())


if __name__ == "__main__":
    import os
    os.environ['DJANGO_SETTINGS_MODULE'] = "settings"
    
    x = Form()
    x.get_fields()