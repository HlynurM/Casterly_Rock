from django.db import models
from django.contrib.auth.models import User

# Estates models
class Kingdom(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class RegionCode(models.Model):
    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)
    region_code = models.IntegerField()

    def __str__(self):
        return str(self.region_code)


class Address(models.Model):
    region_code = models.ForeignKey(RegionCode, on_delete=models.CASCADE)
    street_name = models.CharField(max_length=255)

    def __str__(self):
        return self.street_name


class EstateCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Estates(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=80, blank=True)
    description = models.TextField(blank=True)
    price = models.FloatField()
    category = models.ForeignKey(EstateCategory, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True)
    on_sale = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class EstateImage(models.Model):
    image = models.CharField(max_length=999)
    estate = models.ForeignKey(Estates, on_delete=models.CASCADE)

    def __str__(self):
        return self.image


class EstateDetails(models.Model):
    estate = models.ForeignKey(Estates, on_delete=models.CASCADE)
    size = models.IntegerField()
    rooms = models.IntegerField()
    floors = models.IntegerField()
    towers = models.IntegerField()
    ballroom = models.BooleanField()
    tower_office = models.BooleanField()
    moat = models.BooleanField()
    stables = models.BooleanField()
    dungeon = models.BooleanField()
    drawbridge = models.BooleanField()


class StarRating(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    estate = models.ForeignKey(Estates, on_delete=models.CASCADE)
    has_star = models.BooleanField(default=None)
