from django.forms import ModelForm, widgets
from django import forms
from estates.models import Estates, EstateDetails


class CreateEstateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    moat = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'checkbox'}))
    class Meta:
        model = Estates
        exclude = [ 'id' ]
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'short_description': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'rows': 5, 'cols': 150}),
            'address': widgets.Select(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'user': widgets.Select(attrs={'class': 'form-control'}),
            'on_sale': widgets.CheckboxInput(attrs={'class': 'checkbox'})
        }


class UpdateEstateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Estates
        exclude = [ 'id' ]
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'short_description': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'rows': 4, 'cols': 15}),
            'address': widgets.Select(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'user': widgets.Select(attrs={'class': 'form-control'}),
            'on_sale': widgets.CheckboxInput(attrs={'class': 'checkbox'})
        }

class CreateEstateForm2(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    moat = forms.BooleanField(required=False, widget=forms.RadioSelect(attrs={'class': 'form-control'}))
    class Meta:
        model = EstateDetails
        exclude = [ 'id' ]
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'short_description': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'rows': 5, 'cols': 150}),
            'address': widgets.Select(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'user': widgets.Select(attrs={'class': 'form-control'}),
            'on_sale': widgets.CheckboxInput(attrs={'class': 'checkbox'})
        }