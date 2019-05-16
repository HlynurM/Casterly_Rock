from django.db import models
from django.contrib.auth.models import User
from estates.models import Estates
from user.models import CreditCard


# Sales models
class Client(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE)
    card_num = models.OneToOneField(CreditCard, on_delete=models.CASCADE)

class Owner(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    card_num = models.OneToOneField(CreditCard, on_delete=models.CASCADE)

class Sales(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    # price = models.ForeignKey(Estates.price, on_delete=models.CASCADE)
    price = models.FloatField()
    estate = models.OneToOneField(Estates, on_delete=models.CASCADE)