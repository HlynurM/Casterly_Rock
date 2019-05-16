from django.forms import ModelForm, widgets
from django import forms
from estates.models import Estates, EstateDetails, Address


class CreateEstateForm(ModelForm):
    Slóð_á_mynd = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Estates
        exclude = ['id']
        fields = ['name', 'short_description', 'description', 'address', 'category', 'price', 'user', 'on_sale']
        # fields = ['name', 'short_description', 'description', 'address', 'category', 'price', 'on_sale']
        labels = {
            "name": "Nafn",
            "short_description": "Stutt og hnitmiðuð fyrirsögn",
            "description": "Lýsing á eign",
            "address": "Heimilisfang",
            "category": "Flokkur",
            "price": "Verð á eign",
            "user": "Eigandi",
            "on_sale": "Er eignin á sölu",
        }
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'short_description': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'rows': 10, 'cols': 5}),
            'address': widgets.Select(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'user': widgets.Select(attrs={'class': 'form-control'}),
            'on_sale': widgets.CheckboxInput(attrs={'class': 'checkbox'})
        }


class UpdateEstateForm(ModelForm):
    Slóð_á_mynd = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Estates
        exclude = ['id']
        fields = ['name', 'short_description', 'description', 'address', 'category', 'price', 'user', 'on_sale']
        # fields = ['name', 'short_description', 'description', 'address', 'category', 'price', 'on_sale']
        labels = {
            "name": "Nafn",
            "short_description": "Stutt og hnitmiðuð fyrirsögn",
            "description": "Lýsing á eign",
            "address": "Heimilisfang",
            "category": "Flokkur",
            "price": "Verð á eign",
            "user": "Eigandi",
            "on_sale": "Er eignin á sölu",
        }
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
        labels = {
            "size": "Stærð eignar",
            "rooms": "Herbergjafjöldi",
            "floors": "Hæðir",
            "towers": "Hversu margir turnar",
            "ballroom": "Er danssalur",
            "tower_office": "Er turnskrifstofa",
            "moat": "Er kastala síki",
            "stables": "Eru hesthús",
            "dungeon": "Fylgir dýflissa með",
            "drawbridge": "Er vindubrú",
        }
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
        labels = {
            "size": "Stærð eignar",
            "rooms": "Herbergjafjöldi",
            "floors": "Hæðir",
            "towers": "Hversu margir turnar",
            "ballroom": "Er danssalur",
            "tower_office": "Er turnskrifstofa",
            "moat": "Er kastala síki",
            "stables": "Eru hesthús",
            "dungeon": "Fylgir dýflissa með",
            "drawbridge": "Er vindubrú",
        }
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
