from django.db import models

# from user.models import Users


# class EstatesCategory(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name
#
#
# class Estates(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=999, blank=True)
#     category = models.ForeignKey(EstatesCategory, on_delete=models.CASCADE)
#     price = models.FloatField()
#     on_sale = models.BooleanField()
#     # user = models.ForeignKey('user.Users', on_delete=models.CASCADE)
#
#     def __str__(self):
#         """Returns the name of the object"""
#         return self.name
#
#
# class EstatesImage(models.Model):
#     image = models.CharField(max_length=999)
#     estate = models.ForeignKey(Estates, on_delete=models.CASCADE)
#
#     def __str__(self):
#         """Returns the path and name instead of the object referance"""
#         return self.image


#============================================================================
#============ [ REAL DATABASE ] =============================================
#============================================================================


class Kingdom(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Region_code(models.Model):
    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)
    region_code = models.IntegerField()

    def __str__(self):
        return self.region_code


class Address(models.Model):
    region_code = models.ForeignKey(Region_code, on_delete=models.CASCADE)
    street_name = models.CharField(max_length=255)

    def __str__(self):
        return self.street_name


class Estate_category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Estates(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=80, blank=True)
    description = models.CharField(max_length=999, blank=True)
    price = models.FloatField()
    category = models.ForeignKey(Estate_category, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    on_sale = models.BooleanField()
    user = models.ForeignKey('temp.Users', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Estate_image(models.Model):
    image = models.CharField(max_length=999)
    estate = models.ForeignKey(Estates, on_delete=models.CASCADE)

    def __str__(self):
        return self.image


class Estate_details(models.Model):
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


class Star_rating(models.Model):
    user = models.ForeignKey('temp.Users', on_delete=models.CASCADE)
    estate = models.ForeignKey(Estates, on_delete=models.CASCADE)
