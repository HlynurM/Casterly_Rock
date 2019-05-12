from django.db import models
from django.contrib.auth.models import User
from estates.models import Estates

# Create your models here.
# LOGIN DÓT - profile auka info. munum þurfa fasteign og þess háttar hér
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    owned_property = models.OneToOneField(Estates, on_delete=models.CASCADE)
    # favorite_candy = models.ForeignKey(Candy, on_delete = models.CASCADE)
    profile_image = models.CharField(max_length = 9999)