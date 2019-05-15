from django.forms import ModelForm, widgets
from django import forms
from estates.models import Estates, EstateDetails


class CreateEstateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Estates
        exclude = ['id']
        fields = ['name', 'short_description', 'description', 'address', 'category', 'price', 'user', 'on_sale']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'short_description': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'rows': 5, 'cols': 5}),
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
        exclude = ['id']
        fields = ['name', 'short_description', 'description', 'address', 'category', 'price', 'user', 'on_sale']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'short_description': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'rows': 5, 'cols': 5}),
            'address': widgets.Select(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'user': widgets.Select(attrs={'class': 'form-control'}),
            'on_sale': widgets.CheckboxInput(attrs={'class': 'checkbox'})
        }


class AddDetailsForm(ModelForm):
    class Meta:
        model = EstateDetails
        exclude = ['id', 'estate']
        fields = ['size','rooms','floors','towers','ballroom','tower_office','moat','stables','dungeon','drawbridge']
        widgets = {
            'size': widgets.NumberInput(attrs={'class': 'form-control'}),
            'rooms': widgets.NumberInput(attrs={'class': 'form-control'}),
            'floors': widgets.NumberInput(attrs={'class': 'form-control'}),
            'towers': widgets.NumberInput(attrs={'class': 'form-control'}),
            'ballroom': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'tower_office': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'moat': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'stables': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'dungeon': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'drawbridge': widgets.CheckboxInput(attrs={'class': 'checkbox'})
        }

class UpdateDetailsForm(ModelForm):
    class Meta:
        model = EstateDetails
        exclude = ['id', 'estate']
        fields = ['size','rooms','floors','towers','ballroom','tower_office','moat','stables','dungeon','drawbridge']
        widgets = {
            'size': widgets.NumberInput(attrs={'class': 'form-control'}),
            'rooms': widgets.NumberInput(attrs={'class': 'form-control'}),
            'floors': widgets.NumberInput(attrs={'class': 'form-control'}),
            'towers': widgets.NumberInput(attrs={'class': 'form-control'}),
            'ballroom': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'tower_office': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'moat': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'stables': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'dungeon': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'drawbridge': widgets.CheckboxInput(attrs={'class': 'checkbox'})
        }
