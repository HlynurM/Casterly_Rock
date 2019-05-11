from django.shortcuts import render, get_object_or_404
from estates.forms.new_estate_form import CreateEstateForm
from estates.models import Estates, EstatesImage

def index(request):
    # TODO: Change to order by date by default, then by filter results when we have a filter
    context = {
        'estates': Estates.objects.all().order_by('name')
    }

    return render(request, 'estates/index.html', context)


#TODO: setja upp rouding endapunkta fyrir serstakar eignir
def get_estate_by_id(request, id):
    return render(request, 'estates/estate_overview.html', {
        #GET ONE estate from the request if it exists.
        'estate' : get_object_or_404(Estates, pk=id)
    })

def add_new_estate(request):
    if request.method == 'POST':
        form = CreateEstateForm(data=request.POST)
        if form.is_valid():
            estate = form.save()
            estate_image = EstatesImage(image=request.POST['image'], estate=estate)
            estate_image.save()
            return redirect('estates-index')
    else:
        form = CreateEstateForm()


        context = {
            'form': form
        }
    return render(request, 'estates/add_new_estate.html', context)