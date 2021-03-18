from django.db import models
from django_countries.fields import CountryField


# Create your models here.


class Category(models.Model):
    """ model to add destinations to the db """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class AdventureLocation(models.Model):
    location_name = models.CharField(max_length=100)
    country = CountryField(max_length=100)

    class Meta:
        ordering = ['country']

    def __str__(self):
        return '{}, {}'.format(
            self.location_name, self.country.name
            )
        # return f"{self.location_name}, {self.country.name}"


class Adventure(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL) # SET_NULL Vs CASCADE
    adventure_location = models.ForeignKey('AdventureLocation', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=600)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.IntegerField(null=True, blank=True)
    departure_date = models.DateField(null=True, blank=True)
    departure_time = models.TimeField(null=True, blank=True)
    return_date = models.TimeField(null=True, blank=True)
    slot = models.IntegerField(null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='adventure_images',null=True, blank=True)

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.name
