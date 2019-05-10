from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='estates-index'),
    path('<int:id>', views.get_estate_by_id, name="estate_overview")
]