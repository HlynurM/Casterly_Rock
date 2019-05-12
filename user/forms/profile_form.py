from django.forms import ModelForm, widgets
from user.models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = [ 'id', 'user' ]
        widgets = {
            'profile_image': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'ssn': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'phone': widgets.TextInput(attrs={'class': 'form-control'}),
            'street': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'region_code': widgets.Select(attrs = { 'class': 'form-control' }),
            'kingdom': widgets.Select(attrs = { 'class': 'form-control' }),
            'estates': widgets.Select(attrs = { 'class': 'form-control' }),
            'bio': widgets.TextInput(attrs={'class': 'form-control'}),

        }