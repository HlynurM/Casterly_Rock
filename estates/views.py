from django.shortcuts import render, get_object_or_404
from estates.models import Estates

def index(request):
    # TODO: Change to order by date by default, then by filter results when we have a filter
    context = {'estates': Estates.objects.all().order_by('name')}
    return render(request, 'estates/index.html', context)


#TODO: setja upp rouding endapunkta fyrir serstakar eignir
def get_estate_by_id(request, id):
    return render(request, 'estates/estate_overview.html', {
        #GET ONE estate from the request if it exists.
        'estate' : get_object_or_404(Estates, pk=id)
    })