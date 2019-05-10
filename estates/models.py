from django.db import models

from users.models import Users

class EstatesCategory(models.Model):
    name = models.CharField(max_length=255)

class Estates(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    category = models.ForeignKey(EstatesCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    on_sale = models.BooleanField()
    notendur = models.ForeignKey('users.Users', on_delete=models.CASCADE)
    def __str__(self):
        """Returns the name of the object"""
        return self.name

class EstatesImage(models.Model):
    image = models.CharField(max_length=999)
    estate = models.ForeignKey(Estates, on_delete=models.CASCADE)
    def __str__(self):
        """Returns the path and name instead of the object referance"""
        return self.image

