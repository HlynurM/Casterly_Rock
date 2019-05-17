from django.db import models
from django.contrib.auth.models import User
from estates.models import Address, Estates, RegionCode, Kingdom


# User models
# class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # owned_property = models.OneToOneField('Estates', on_delete=models.CASCADE)
    # profile_image = models.CharField(max_length=999)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ssn = models.CharField(max_length=11, blank=True, unique=False)
    phone = models.CharField(max_length=7, blank=True)
    street = models.CharField(max_length=255, unique=False, blank=True)
    region = models.ForeignKey(RegionCode, default=1 , on_delete=models.CASCADE)
    kingdom = models.ForeignKey(Kingdom, default=1, on_delete=models.CASCADE)
    #address = models.ForeignKey(Address, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_image = models.CharField(max_length=999, blank=True)
    #owned_property = models.OneToOneField(Estates, on_delete=models.CASCADE)
    #profile_image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class CreditCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    credit_number = models.CharField(max_length=19)
    sec_number = models.IntegerField(default=None)
    credit_amount = models.FloatField(null=True, blank=True)