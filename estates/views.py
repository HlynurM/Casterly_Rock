from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.db.models import Q
from estates.forms.new_estate_form import CreateEstateForm, UpdateEstateForm, AddressForm, RegionForm, KingdomForm
from estates.models import Estates, EstateImage, StarRating
from django.contrib import messages


def index(request):
    '''Forsiduyfirlit'''
    if 'search_filter' in request.GET:
        search_filter = request.GET.get('search_filter', '')
        estates = [{
            'id': x.id,
            'name': x.name,
            'description': x.short_description,
            #dropdown
            'price': x.price,
            'size': x.size,
            'floors': x.floors,
            'rooms': x.rooms,
            #checkbox
            'on_sale':x.on_sale,

            # 'category': x.category,
            'firstImage': x.estateimage_set.first().image
        } for x in Estates.objects.filter(
            Q(name__icontains=search_filter) or
            Q(description__icontains=search_filter) or
            Q(price__icontains=search_filter) or
            Q(category__name__icontains=search_filter) or
            Q(moat__in=search_filter) or
            Q(address__street_name__icontains=search_filter) or
            Q(address__region_code__icontains=search_filter) or
            Q(address__region_code__kingdom___icontains=search_filter)

        )]
        # print(estates)
        return JsonResponse({'data': estates})
    context = {
        'estates': Estates.objects.all().order_by('name')
    }
    return render(request, 'estates/index.html', context)


def get_estate_by_id(request, id):
    '''Gets an estate by id if it exists'''
    return render(request, 'estates/estate_overview.html', {
        # GET ONE estate from the request if it exists.
        'estate': get_object_or_404(Estates, pk=id)
    })


def add_new_estate(request):
    if request.method == 'POST':
        estate_form = CreateEstateForm(data=request.POST)
        #region_form = RegionForm(data=request.POST)
        #address_form = AddressForm(data=request.POST)
        #kingdom_form = KingdomForm(data=request.POST)

        #if estate_form.is_valid() and region_form.is_valid():
        if estate_form.is_valid():
            estate = estate_form.save()  # save the form into database
            #region_form.save()

            estate_image = EstateImage(image=request.POST['Slóð_á_mynd'], estate=estate)
            if estate_image.image != "":
                estate_image.save()  # save the image into database
            messages.success(request, f'Skráning á eign tókst.')
            return redirect('estates-index')
    else:
        estate_form = CreateEstateForm()
        #region_form = RegionForm()


    context = {
        'estate_form': estate_form,
        #'region_form': region_form,

    }
    return render(request, 'estates/add_new_estate.html', context)


def remove_estate(request, id):
    estate = get_object_or_404(Estates, pk=id)
    estate.delete()
    messages.success(request, f'Eign fjarlægð.')
    return redirect('estates-index')



def update_estate(request, id):
    the_estate = get_object_or_404(Estates, pk=id)

    if request.method == 'POST':
        estate_form = UpdateEstateForm(data=request.POST, instance=the_estate)

        if estate_form.is_valid():
            estate = estate_form.save()
            estate_image = EstateImage(image=request.POST['Slóð_á_mynd'], estate=estate)
            if estate_image.image != "":
                estate_image.save()  # save the image into database
            messages.success(request, f'Eign uppfærð.')
            return redirect('estate_overview', id=id)
    else:

        estate_form = UpdateEstateForm(instance=the_estate)

    context = {
        'estate_form': estate_form,
        'id': id
    }
    return render(request, 'estates/update_estate.html', context)
