from django.shortcuts import render, get_object_or_404, redirect
# from django.http import JsonResponse
# from sales.models import Sales
from sales.forms.new_sale import NewCreditCardForm
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        form = CreateEstateForm(data=request.POST)
        if form.is_valid():
            estate = form.save()    #save the form into database
            estate_image = EstateImage(image=request.POST['image'], estate=estate)
            estate_image.save()     #save the image into database
            return redirect('estates-index')
    else:
        form = CreateEstateForm()

    context = {
        'form': form
    }
    return render(request, 'estates/add_new_estate.html', context)


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

