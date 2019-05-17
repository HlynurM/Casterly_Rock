from django.forms import ModelForm, widgets
from django import forms
from sales.models import Sales
from user.models import CreditCard


class NewCreditCardForm(ModelForm):
    class Meta:
        model = CreditCard
        exclude = ['id']
        fields = ['credit_number',
                  'sec_number',
                  # 'credit_amount',
                  'user']
        labels = {
            "credit_number": "Kortanúmer",
            "sec_number": "Öryggisnúmer",
            # "credit_amount": "Upphæð",
            "user": "Eigandi"
        }
        widgets = {
            'credit_number': widgets.NumberInput(attrs={'class': 'form-control col-md-12'}),
            'sec_number': widgets.NumberInput(attrs={'class': 'form-control col-md-6'}),
            # 'credit_amount': widgets.NumberInput(attrs={'class': 'form-control col-md-6'}),
            'user': widgets.Select(attrs={'class': 'form-control col-md-6'})
        }
