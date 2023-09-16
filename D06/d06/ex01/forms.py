import re

from django import forms
from django.contrib.auth.models import User
from .models import Tip

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")

        username = cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists.")

        if password:
            # Password complexity check using regular expression
            # Ensure the password contains at least one digit, one uppercase letter, and one special character
            if not re.match(r'^(?=.*\d)(?=.*[A-Z])(?=.*[@#$%^&+=!]).*$', password):
                raise forms.ValidationError("Password must contain at least one digit, one uppercase letter, and one special character (@#$%^&+=!).")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ['content']