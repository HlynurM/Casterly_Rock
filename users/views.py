from django.shortcuts import render
from users.models import Users

def index(request):
    return render(request, 'users/../templates/user/index.html', {
        'users':  Users.objects.all()
    })