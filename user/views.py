# Create your views here.
from django.shortcuts import render, redirect
from user.forms.profile_form import ProfileForm, UserForm
from user.forms.register_form import UserRegisterForm
from user.models import UserProfile
from django.contrib import messages


def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Notandi {username} skráður!')
            form.save()
            return redirect('/')
        else:
            messages.error(request, f'Villa við skráningu! Vinsamlegast fylgið leiðbeiningum')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {
        'form': form,

    })

# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error

def profile(request):

    #u_profile = UserProfile.objects.filter(user = request.user).first()
    if request.method == 'POST':
        u_form = UserForm(request.POST, instance=request.user)
        #p_form = ProfileForm(request.POST, instance=request.user.userprofile)
        p_form = ProfileForm()

        #if p_form.is_valid() and u_form.is_valid():
        if u_form.is_valid() and p_form.is_valid():
            # .save gerir commit by default - en hér uppfærum við user foreign key áður en við committum...

            profile = p_form.save(commit = False)
            profile.user = request.user
            profile.save()
            u_profile = u_form.save(commit = False)
            u_profile.user = request.user
            u_profile.save()
            return redirect('profile')
        else:
            messages.error(request, f'Villa við skráningu! Vinsamlegast fylgið leiðbeiningum')

    else:
        u_form = UserForm(instance = request.user)
        p_form = ProfileForm()


    return render(request, 'user/profile.html', {
        'p_form': p_form,
        'u_form': u_form
    })


def index(request):
    return render(request, 'user/index.html', {
        'user':  Users.objects.all()
    })