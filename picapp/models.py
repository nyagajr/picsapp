from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length =30)

    def __str__(self):
        return self.category_name


class Location(models.Model):
    loc_name = models.CharField(max_length =30)

    def __str__(self):
        return self.loc_name

class Image(models.Model):
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =50)
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)
