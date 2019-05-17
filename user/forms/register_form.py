from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    #email = forms.EmailField()

    # leyfir enn skráningu á sömu emailum!!!

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
            ]
        labels = {
            "username": "Notendanafn",
            "email": "Netfang",
            "first_name": "Fornafn",
            "last_name": "Ættarnafn",
            "password1": "Lykilorð",
            "password2": "Staðfesta lykilorð",
        }
