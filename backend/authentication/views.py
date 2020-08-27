from django.contrib.auth.views import LoginView
from . import forms

class UserLoginView(LoginView):
    template_name = "login.html"
    form_class = forms.AuthenticationForm