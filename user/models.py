from django.db import models
from django.contrib.auth.models import User
from estates.models import Address, Estates


# User models
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # owned_property = models.OneToOneField('Estates', on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=999)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, unique=True)
    ssn = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=7)
    profile_image = models.CharField(max_length=999, blank=True)
    owned_property = models.OneToOneField(Estates, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)


class CreditCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit_number = models.CharField(max_length=19)
    sec_number = models.IntegerField()
    credit_amount = models.FloatField()