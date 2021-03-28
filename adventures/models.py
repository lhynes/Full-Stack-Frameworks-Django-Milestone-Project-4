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
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    slot = models.IntegerField(null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='adventure_images',null=True, blank=True)

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.name

    def get_number_bought_since_date(self, date_from):
        Sum = None
        print(OrderLineItem.objects.filter(Q(adventure_id=self.id) & Q(created_at__greater_than=date_from)).aggregate(Sum('quantity')))
