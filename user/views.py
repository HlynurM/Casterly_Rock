# Create your views here.
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from estates.models import Estates
from user.forms.profile_form import ProfileForm, UserForm
from user.forms.register_form import UserRegisterForm
from django.contrib.auth.decorators import login_required
from user.models import UserProfile
from django.contrib import messages
from user.models import User


def register(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(data = request.POST)
        if u_form.is_valid():
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'Notandi {username} skráður!')
            u_form.save()
            return redirect('/')
        else:
            messages.error(request, f'Villa við skráningu! Vinsamlegast fylgið leiðbeiningum')
    else:
        u_form = UserRegisterForm()
    return render(request, 'user/register.html', {
        'form': u_form,
    })

@login_required
def profile(request):
    profile = UserProfile.objects.filter(user = request.user).first()
    if request.method == 'POST':

        u_form = UserForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, instance=profile)

        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            profile = p_form.save(commit = False)
            profile.user = request.user
            profile.save()
            messages.success(request, f'Breytingar skráðar.')

            return redirect('profile')
        else:
            messages.error(request, f'Eitthvað fór úrskeiðis')
            return redirect('/')
    else:
        u_form = UserForm(instance = request.user)
        p_form = ProfileForm(instance = profile)

    return render(request, 'user/profile.html', {
        'p_form': p_form,
        'u_form': u_form
    })


def index(request):
    return render(request, 'user/index.html', {
        'user':  User.objects.all()
    })

def my_estates(request):
    '''Forsiduyfirlit'''
    myuserid = UserProfile.objects.filter(user = request.user).first().user.id
    myestates = []
    for estate in Estates.objects.filter():
        if estate.user_id == myuserid:
            print(estate)
            myestates.append(estate)

    return render(request, 'user/my_estates.html', myestates)


    if 'search_filter' in request.GET:
        search_filter = request.GET.get('search_filter', '')
        estates = [{
            'id': x.id,
            'name': x.name,
            'description': x.short_description,
            'price': x.price,
            # 'address': x.address,
            'firstImage': x.estateimage_set.first().image
        } for x in Estates.objects.filter(
            Q(name__icontains=search_filter) or
            Q(description__icontains=search_filter) or
            Q(price__icontains=search_filter) or
            Q(address__street_name__icontains=search_filter) or
            Q(address__region_code__icontains=search_filter) or
            Q(address__region_code__kingdom___icontains=search_filter)

        )]
        # print(estates)
        return JsonResponse({'data': estates})
    context = {
        'estates': Estates.objects.all().order_by('name')
    }
    return render(request, 'user/my_estates.html', context)