from django.forms import ModelForm, widgets
from django import forms
from sales.models import Sales
from user.models import CreditCard

class NewCreditCardForm(ModelForm):
    class Meta:
        model = Sales
        exclude = [ 'id' ]
        # fields = [
        #     'credit_number',
        #     'sec_number',
        #     'credit_amount'
        # ]
        widgets = {
            'credit_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'sec_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'credit_amount': widgets.NumberInput(attrs={'class': 'form-control'})
        }