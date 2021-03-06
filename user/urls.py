from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('', views.index, name='user-index'),
    path('register', views.register, name = 'register'),
    path('login', LoginView.as_view(template_name = 'user/login.html'), name = 'login'),
    path('logout', LogoutView.as_view(next_page = '/'), name = 'logout'),
    path('profile', views.profile, name='profile'),
    path('my_estates', views.my_estates, name = 'my_estates')
]