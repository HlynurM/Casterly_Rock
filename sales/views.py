from django.shortcuts import render, get_object_or_404, redirect
# from django.http import JsonResponse
# from sales.models import Sales
from sales.forms.new_sale import NewCreditCardForm
from django.contrib import messages


# Create your views here.
def new_sale(request):
    if request.method == 'POST':
        form = NewCreditCardForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Skráning hefur tekist!')
            return redirect('/')
        else:
            messages.error(request, f'Einhver villa hefur komið upp við skráningu. Fylgjið leiðbeiningum')
    else:
        form = NewCreditCardForm()

    context = {
        'form': form
    }
    return render(request, 'sales/new_sale.html', context)