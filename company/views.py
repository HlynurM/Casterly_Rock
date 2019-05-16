from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse


# Create your views here.
def about(request):
    """Sendir okkur a """
    return render(request, 'company/about.html')