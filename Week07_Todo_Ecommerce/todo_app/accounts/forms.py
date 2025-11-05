from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

        widgets = {
            'username': forms.TextInput(attrs={
                "class":"form-control",
                "placeholder" : "Enter your username",
            }),
            'email': forms.EmailInput(attrs={  # <-- Correct
                "class":"form-control",
                "placeholder": "Enter your Email",
            }),
            'password1':forms.PasswordInput(attrs={
                "class":"form-control",
                "placeholder": "Enter your Password",
            }),
            'password2':forms.PasswordInput(attrs={
                "class":"form-control",
                "placeholder": "Confirm your Password",
            }),
        }
