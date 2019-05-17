from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='estate-index'),
    path('<int:id>', views.start_sale, name='sale-index'),
    path('card_info/<int:id>', views.new_card_info, name='sale-card-info'),
    path('confirm/<int:id>', views.sale_confirm, name='sale-confirm'),
    path('thankyou/<int:id>', views.thank_you, name='sale-thank-you')

]