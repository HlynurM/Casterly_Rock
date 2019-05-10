from django.shortcuts import render
from users.models import Users

def index(request):
    return render(request, 'users/index.html', {
        'users':  Users.objects.all()
    })