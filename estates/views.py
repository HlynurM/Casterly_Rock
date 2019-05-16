from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.db.models import Q
from estates.forms.new_estate_form import *
from estates.models import *

def index(request):
    '''Forsiduyfirlit'''
    if 'search_filter' in request.GET:
        search_filter = request.GET.get('search_filter', '')
        estates = [ {
            'id': x.id,
            'name': x.name,
            'description': x.short_description,
            'on_sale': x.on_sale,
            'price': x.price,
            'firstImage': x.estateimage_set.first().image,





            # 'rooms': x.estatedetails_set.first().rooms,
            # 'floors': x.estatedetails_set.first().floors,
            # 'towers': x.estatedetails_set.first().towers,
            # 'ballroom': x.estatedetails_set.first().ballroom,
            # 'tower_office': x.estatedetails_set.first().tower_office,
            # 'moat': x.estatedetails_set.first().moat



        } for x in Estates.objects.filter(name__icontains=search_filter
            # Q(name__icontains=search_filter) or
            # Q(description__icontains=search_filter) or
            # Q(address__region_code__icontains=search_filter) or
            # Q(address__street_name__icontains=search_filter)
        )]




        return JsonResponse({'data': estates})

    # estates_details = [{
    #     'size': x.size,
    #    'floors': x.floors,
    #    'moat': x.moat
    #
    # } for x in EstateDetails.objects]


    context = {'estates': Estates.objects.all().order_by('name')}
    return render(request, 'estates/index.html', context)

    #
    #     #kalla á estate_datails.
    #     search_filter_details = request.GET.get('search_filter', '')
    #     estate_details = [ {
    #         'estate': x.estate,
    #         'size': x.size,
    #         'rooms': x.rooms,
    #         'floors': x.floors,
    #         'towers': x.towers,
    #         'ballroom': x.ballroom,
    #         'tower_office': x.tower_office,
    #         'moat': x.moat,
    #         'stables': x.stables,
    #         'dungeon': x.dungeon,
    #         'drawbridge': x.drawbridge
    #     } for x in EstateDetails.objects.filter(name__icontains=search_filter_details)
    #
    #     ]
    #
    #
    #     return JsonResponse({ 'data': estates})
    # context = { 'estates': Estates.objects.all().order_by('name') }
    # return render(request, 'estates/index.html', context)





def get_estate_by_id(request, id):
    '''Gets an estate by id if it exists'''
    return render(request, 'estates/estate_overview.html', {
        #GET ONE estate from the request if it exists.
        'estate' : get_object_or_404(Estates, pk=id)
    })

def add_new_estate(request):
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

def remove_estate(request, id):
    estate = get_object_or_404(Estates, pk=id)
    estate.delete()
    return redirect('estates-index')

def update_estate(request, id):
    the_estate = get_object_or_404(Estates, pk=id)
    if request.method == 'POST':
        form = UpdateEstateForm(data=request.POST, instance=the_estate)
        if form.is_valid():
            form.save()
            return redirect('estate_overview', id=id)
    else:
        form = UpdateEstateForm(instance=the_estate)

    context = {
        'form': form,
        'id': id
    }
    return render(request, 'estates/update_estate.html', context)