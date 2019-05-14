from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='estate-index'),
    path('new_sale', views.new_sale, name='new_sale')
]