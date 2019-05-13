from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from user.forms.profile_form import ProfileForm
from user.forms.register_form import UserRegisterForm
from user.models import Profile
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Notandi {username} skráður!')
            form.save()
            return redirect('/')
        else:
            messages.error(request, f'Villa við skráningu! Vinsamlegast fylgið leiðbeiningum')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {
        'form': form
    })

def profile(request):
    profile = Profile.objects.filter(user = request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance = profile, data = request.POST)
        if form.is_valid():
            # .save gerir commit by default - en hér uppfærum við user foreign key áður en við committum...
            profile = form.save(commit = False)
            profile.user = request.user
            profile.save()
            return redirect('profile')

    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance = profile)
    })

