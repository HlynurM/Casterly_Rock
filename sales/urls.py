from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='estate-index'),
    path('<int:id>', views.start_sale, name='sale-index'),
    path('card_info/<int:id>', views.new_cart_info, name='sale-card-info')

]