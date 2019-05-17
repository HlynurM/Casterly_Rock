from django import forms
from django.forms import widgets, ModelForm
from user.models import UserProfile
from django.contrib.auth.models import User


class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['id', 'user']
        #field = ['profile_image']
        widgets = {
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'}),
            'ssn': widgets.TextInput(attrs={'class': 'form-control'}),
            'phone': widgets.TextInput(attrs={'class': 'form-control'}),
            'street': widgets.TextInput(attrs={'class': 'form-control'}),
            'region': widgets.Select(attrs={'class': 'form-control'}),
            'kingdom': forms.widgets.Select(attrs = { 'class': 'form-control' }),
            #'estates': widgets.Select(attrs={'class': 'form-control'}),
            'bio': widgets.Textarea(attrs={'rows': 5, 'cols': 5}),
        }
        labels = {
            "profile_image": "Slóð á ljósmynd",
            "ssn": "Kennitala",
            "phone": "Símanúmer",
            "street": "Heimilisfang",
            "bio": "Lýsing á þér",
            "region": "Póstnúmer",
            "kingdom": "Hérað",
        }
class UserForm(ModelForm):
    #email = forms.EmailField()
    class Meta:
        model = User
        exclude = ['id', 'user']
        fields = ['first_name', 'last_name', 'email']
        labels = {
            "first_name": "Fornafn",
            "last_name": "Ættarnafn",
            "email": "Netfang",
        }
