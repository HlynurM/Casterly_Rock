from django.forms import ModelForm, widgets
from django import forms
from estates.models import Estates, EstateDetails, Address, Kingdom

class CreateEstateForm(ModelForm):
    #völdum þennan titil á breytunafn til að það myndi birtast á íslensku í formi á vef
    Slóð_á_mynd = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Estates
        exclude = ['id']
        fields = ['name',
                  'user',
                  'short_description',
                  'description',
                  'Slóð_á_mynd',
                  'size',
                  'rooms',
                  'floors',
                  'towers',
                  'ballroom',
                  'tower_office',
                  'moat',
                  'stables',
                  'dungeon',
                  'drawbridge',
                  'address',
                  'category',
                  'price']
        # fields = ['name', 'short_description', 'description', 'address', 'category', 'price', 'on_sale']
        labels = {
            "name": "Nafn",
            "short_description": "Stutt og hnitmiðuð fyrirsögn",
            "description": "Lýsing á eign",
            "address": "Heimilisfang",
            "category": "Flokkur",
            "price": "Verð á eign í €",
            "user": "Eigandi",
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
            'name': widgets.TextInput(attrs={'class': 'form-control col-md-12'}),
            'short_description': widgets.TextInput(attrs={'class': 'form-control col-md-12'}),
            'description': widgets.Textarea(attrs={'rows': 10, 'cols': 5}),
            'address': widgets.Select(attrs={'class': 'form-control col-md-6 mb-3'}),
            'category': widgets.Select(attrs={'class': 'form-control col-md-6 mb-3'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control col-md-6'}),
            'user': widgets.Select(attrs={'class': 'form-control col-md-6'}),

            'size': widgets.NumberInput(attrs={'class': 'form-control col-md-6'}),
            'rooms': widgets.NumberInput(attrs={'class': 'form-control col-md-6'}),
            'floors': widgets.NumberInput(attrs={'class': 'form-control col-md-6'}),
            'towers': widgets.NumberInput(attrs={'class': 'form-control col-md-6'}),
            'ballroom': widgets.CheckboxInput(attrs={'class': 'checkbox col-md-6'}),
            'tower_office': widgets.CheckboxInput(attrs={'class': 'checkbox col-md-6'}),
            'moat': widgets.CheckboxInput(attrs={'class': 'checkbox col-md-6'}),
            'stables': widgets.CheckboxInput(attrs={'class': 'checkbox col-md-6'}),
            'dungeon': widgets.CheckboxInput(attrs={'class': 'checkbox col-md-6'}),
            'drawbridge': widgets.CheckboxInput(attrs={'class': 'checkbox col-md-6'})
        }


class UpdateEstateForm(ModelForm):
    Slóð_á_mynd = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Estates
        exclude = ['id', 'user']
        fields = ['name',
                  'short_description',
                  'description',
                  'Slóð_á_mynd',
                  'size',
                  'rooms',
                  'floors',
                  'towers',
                  'ballroom',
                  'tower_office',
                  'moat',
                  'stables',
                  'dungeon',
                  'drawbridge',
                  'address',
                  'category',
                  'price',]
        labels = {
            "name": "Nafn",
            "short_description": "Stutt og hnitmiðuð fyrirsögn",
            "description": "Lýsing á eign",
            "address": "Heimilisfang",
            "category": "Flokkur",
            "price": "Verð á eign",
            "user": "Eigandi",
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
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'short_description': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'rows': 10, 'cols': 5}),
            'address': widgets.Select(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'user': widgets.Select(attrs={'class': 'form-control'}),

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


class AddressForm(ModelForm):
    class Meta:
        model = Address
        exclude = ['id', 'user']
        fields = ['street_name']
        labels = {
            "street_name": "Gata",
        }

class RegionForm(ModelForm):
    class Meta:
        model = Address
        exclude = ['id', 'user']
        widgets = {
            'region_code': widgets.Select(attrs={'class': 'form-control'}),
            'kingdom': widgets.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            "region_code": "Póstnúmer",
            "street_name": "Gata"
        }

class KingdomForm(ModelForm):
    class Meta:
        model = Kingdom
        exclude = ['id', 'user']
        widgets = {
        }
        labels = {
            "kingdom": "Hérað",

        }

# class AddDetailsForm(ModelForm):
#     class Meta:
#         model = EstateDetails
#         exclude = ['id', 'estate']
#         fields = ['size','rooms','floors','towers','ballroom','tower_office','moat','stables','dungeon','drawbridge']
#         labels = {
#             "size": "Stærð eignar",
#             "rooms": "Herbergjafjöldi",
#             "floors": "Hæðir",
#             "towers": "Hversu margir turnar",
#             "ballroom": "Er danssalur",
#             "tower_office": "Er turnskrifstofa",
#             "moat": "Er kastala síki",
#             "stables": "Eru hesthús",
#             "dungeon": "Fylgir dýflissa með",
#             "drawbridge": "Er vindubrú",
#         }
#         widgets = {
#             'size': widgets.NumberInput(attrs={'class': 'form-control'}),
#             'rooms': widgets.NumberInput(attrs={'class': 'form-control'}),
#             'floors': widgets.NumberInput(attrs={'class': 'form-control'}),
#             'towers': widgets.NumberInput(attrs={'class': 'form-control'}),
#             'ballroom': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
#             'tower_office': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
#             'moat': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
#             'stables': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
#             'dungeon': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
#             'drawbridge': widgets.CheckboxInput(attrs={'class': 'checkbox'})
#         }
#
# class UpdateDetailsForm(ModelForm):
#     class Meta:
#         model = EstateDetails
#         exclude = ['id', 'estate']
#         fields = ['size','rooms','floors','towers','ballroom','tower_office','moat','stables','dungeon','drawbridge']
#         labels = {
#             "size": "Stærð eignar",
#             "rooms": "Herbergjafjöldi",
#             "floors": "Hæðir",
#             "towers": "Hversu margir turnar",
#             "ballroom": "Er danssalur",
#             "tower_office": "Er turnskrifstofa",
#             "moat": "Er kastala síki",
#             "stables": "Eru hesthús",
#             "dungeon": "Fylgir dýflissa með",
#             "drawbridge": "Er vindubrú",
#         }
#         widgets = {
#             'size': widgets.NumberInput(attrs={'class': 'form-control'}),
#             'rooms': widgets.NumberInput(attrs={'class': 'form-control'}),
#             'floors': widgets.NumberInput(attrs={'class': 'form-control'}),
#             'towers': widgets.NumberInput(attrs={'class': 'form-control'}),
#             'ballroom': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
#             'tower_office': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
#             'moat': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
#             'stables': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
#             'dungeon': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
#             'drawbridge': widgets.CheckboxInput(attrs={'class': 'checkbox'})
#         }
