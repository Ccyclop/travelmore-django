from users.models import User
from django import forms
from django.forms import TextInput, ClearableFileInput, EmailInput, PasswordInput

class User_creation_form(forms.ModelForm):
    def save(self, commit:bool = False):
        user = super().save(False)
        user.set_password(user.password)

        if commit:
            user.save()

        return user

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password', 'avatar',]
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Username'
                }),
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Name'
                }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Last Name'
                }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Email. example@example.com'
                }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Password'
                }),
            'avatar': ClearableFileInput(attrs={
                'class': 'form-control',
                })
            
        }