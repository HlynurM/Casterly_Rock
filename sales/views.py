from django.shortcuts import render, get_object_or_404, redirect
from estates.models import Estates, EstateImage, EstateDetails
from django.contrib.auth.models import User
# from django.http import JsonResponse
# from sales.models import Sales
from sales.forms.new_sale import NewCreditCardForm
from django.contrib import messages


# Create your views here.
def start_sale(request, id):
    """TODO: Starts the sale with the correct Estate selected"""

    print(f'ID of sale is: {id}.')

    context = {
        'estate': get_object_or_404(Estates, pk=id)
    }
    return render(request, 'sales/new_sale.html', context)


def new_cart_info(request, id):
    """TODO: Get info on user and estate"""
#     if request.method == 'POST':
#         form = NewCreditCardForm(data = request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Skráning hefur tekist!')
#             return redirect('/')
#         else:
#             messages.error(request, f'Einhver villa hefur komið upp við skráningu. Fylgjið leiðbeiningum')
#     else:
#         form = NewCreditCardForm()
#
    context = {
        'estate': get_object_or_404(Estates, pk=id),
        'user_info': get_object_or_404(User, pk=id),
    }
    return render(request, 'sales/new_sale.html', context)
