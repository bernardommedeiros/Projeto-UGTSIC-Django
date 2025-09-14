from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    avatar_url = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'avatar_url', 'password1', 'password2']