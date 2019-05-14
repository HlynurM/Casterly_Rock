from django.db import models
from django.contrib.auth.models import User
from estates.models import *



# Create your models here.
# LOGIN DÓT - profile auka info. munum þurfa fasteign og þess háttar hér
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # owned_property = models.OneToOneField('Estates', on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=999, blank=True)


# class Users(models.Model):
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     photo = models.CharField(max_length=999, blank=True)
#     date_of_signup = models.DateTimeField()
#
#     def __str__(self):
#         return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # region_code = models.OneToOneField(Estates.address.region_code, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    #address = models.ForeignKey(Estates.address, on_delete=models.CASCADE)
    ssn = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=7)
    profile_image = models.CharField(max_length=999, blank=True)
    # owned_property = models.OneToOneField('Estates', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)


class CreditCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit_number = models.CharField(max_length=19)
