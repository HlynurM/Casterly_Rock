from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.db.models import Q
from estates.forms.new_estate_form import CreateEstateForm, UpdateEstateForm, AddDetailsForm, UpdateDetailsForm
from estates.models import Estates, EstateImage, EstateDetails, StarRating


def index(request):
    '''Forsiduyfirlit'''
    if 'search_filter' in request.GET:
        search_filter = request.GET.get('search_filter', '')
        estates = [{
            'id': x.id,
            'name': x.name,
            'description': x.short_description,
<<<<<<< HEAD
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
=======
            'price': x.price,
            'firstImage': x.estateimage_set.first().image,
            'rating': x.StarRating.has_star
        } for x in Estates.objects.filter(
            Q(name__icontains=search_filter) or
            Q(description__icontains=search_filter) or
            Q(address__region_code__icontains=search_filter) or
            Q(address__street_name__icontains=search_filter)
        )]
        # print(estates)
        return JsonResponse({'data': estates})
    context = {
        'estates': Estates.objects.all().order_by('name')
    }
>>>>>>> 7035711d43ae1dd475f7651ac3211e80f14622e6
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
        # GET ONE estate from the request if it exists.
        'estate': get_object_or_404(Estates, pk=id)
    })


def add_new_estate(request):
    if request.method == 'POST':
        add_estate_form = CreateEstateForm(data=request.POST)
        add_details_form = AddDetailsForm(data=request.POST)

        if add_estate_form.is_valid() and add_details_form.is_valid():
            estate = add_estate_form.save()  # save the form into database
            details = add_details_form.save(commit=False)
            details.estate = estate
            add_details_form.save()

            estate_image = EstateImage(image=request.POST['image'], estate=estate)
            estate_image.save()  # save the image into database
            return redirect('estates-index')
    else:
        estate_form = CreateEstateForm()
        details_form = AddDetailsForm()

    context = {
        'estate_form': estate_form,
        'details_form': details_form,
    }
    return render(request, 'estates/add_new_estate.html', context)


def remove_estate(request, id):
    estate = get_object_or_404(Estates, pk=id)
    estate.delete()
    return redirect('estates-index')

def update_estate(request, id):
    the_estate = get_object_or_404(Estates, pk=id)
    the_details = get_object_or_404(EstateDetails, estate_id=id)
    # images = get_object_or_404(EstateImage, estate_id=id)

    if request.method == 'POST':
        update_estate_form = UpdateEstateForm(data=request.POST, instance=the_estate)
        update_details_form = UpdateDetailsForm(data=request.POST, instance=the_details)
        # print(f'estate: {update_estate_form}, details: {update_details_form}')

        if update_estate_form.is_valid() and update_details_form.is_valid():
            print("Both are valid!")
            estate = update_estate_form.save()
            details = update_details_form.save(commit=False)
            details.estate=estate
            update_details_form.save()

            return redirect('estate_overview', id=id)
    else:
        print("Or else!!!")
        estate_form = UpdateEstateForm(instance=the_estate)
        details_form = UpdateDetailsForm(instance=the_details)
        # images = UpdateEstateForm(EstateImage, estate_id=id)

    context = {
        'estate_form': estate_form,
        'details_form': details_form,
        'id': id
    }
    return render(request, 'estates/update_estate.html', context)

# def update_estate(request, id):
#     the_estate = get_object_or_404(Estates, pk=id)
#     if request.method == 'POST':
#         form = UpdateEstateForm(data=request.POST, instance=the_estate)
#         if form.is_valid():
#             form.save()
#             return redirect('estate_overview', id=id)
#     else:
#         form = UpdateEstateForm(instance=the_estate)
#
#     context = {
#         'form': form,
#         'id': id
#     }
#     return render(request, 'estates/update_estate.html', context)
