from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='estate-index'),
    path('sale/<int:id>', views.index, name='sale-index')
]