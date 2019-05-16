from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
from estates.models import *


=======
from estates.models import Address, Estates
>>>>>>> 7035711d43ae1dd475f7651ac3211e80f14622e6


# User models
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # owned_property = models.OneToOneField('Estates', on_delete=models.CASCADE)
<<<<<<< HEAD
    profile_image = models.CharField(max_length=999, blank=True)


# class Users(models.Model):
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     photo = models.CharField(max_length=999, blank=True)
#     date_of_signup = models.DateTimeField()
#
#     def __str__(self):
#         return self.name
=======
    profile_image = models.CharField(max_length=999)
>>>>>>> 7035711d43ae1dd475f7651ac3211e80f14622e6


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
<<<<<<< HEAD

    # region_code = models.OneToOneField(Estates.address.region_code, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    #address = models.ForeignKey(Estates.address, on_delete=models.CASCADE)
=======
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
>>>>>>> 7035711d43ae1dd475f7651ac3211e80f14622e6
    ssn = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=7)
    profile_image = models.CharField(max_length=999, blank=True)
    owned_property = models.OneToOneField(Estates, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)


class CreditCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit_number = models.CharField(max_length=19)
    sec_number = models.IntegerField(default=None)
    credit_amount = models.FloatField(default=None)