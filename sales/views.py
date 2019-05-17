from django.shortcuts import render, get_object_or_404, redirect
from estates.models import Estates, EstateImage, EstateDetails
from django.contrib.auth.models import User
# from django.http import JsonResponse
# from sales.models import Sales
from sales.forms.new_sale_form import NewCreditCardForm
from django.contrib import messages


# Create your views here.
def start_sale(request, id):
    """TODO: Starts the sale with the correct Estate selected"""

    context = {
        'estate': get_object_or_404(Estates, pk=id),
        'client': request.user
    }
    return render(request, 'sales/new_sale.html', context)


def new_card_info(request, id):
    if request.method == 'POST':
        kredit_form = NewCreditCardForm(data=request.POST)
        print(f'fyllt kreditform {kredit_form}')
        if kredit_form.is_valid():
            estate = kredit_form.save()  # save the form into database
            messages.success(request, f'Skráning á eign tókst.')
            return redirect('sale-confirm')
    else:
        # print("kredit form")
        kredit_form = NewCreditCardForm()
        # print(f'inside kredit form {kredit_form}')
    #
    context = {
        'estate': get_object_or_404(Estates, pk=id),
        'client': request.user,
        'kredit_form': kredit_form
    }
    return render(request, 'sales/credit_card.html', context)


def sale_confirm(request, id):
    """TODO: Starts the sale with the correct Estate selected"""

    context = {
        'estate': get_object_or_404(Estates, pk=id),
        'client': request.user
    }
    return render(request, 'sales/sale_confirm.html', context)


def thank_you(request, id):
    """TODO: Starts the sale with the correct Estate selected"""

    context = {
        'estate': get_object_or_404(Estates, pk=id),
        'client': request.user
    }
    return render(request, 'sales/sale_thank_you.html', context)
