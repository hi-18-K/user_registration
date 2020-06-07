from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()      #has a default required=True can change

    class Meta:         #gives nested namespace configrations
        model = User
        fields = ['username', 'email', 'password1', 'password2']
