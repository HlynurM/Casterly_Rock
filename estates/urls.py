from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='estates-index'),
    path('<int:id>', views.get_estate_by_id, name="estate_overview"),
    path('add_new_estate', views.add_new_estate, name="add_new_estate")
]