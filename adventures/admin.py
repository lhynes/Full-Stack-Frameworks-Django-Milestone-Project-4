from django.contrib import admin
from .models import Adventure, Category, AdventureLocation

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class AdventureLocationAdmin(admin.ModelAdmin):
    list_display = (
        'location_name',
        'country',
    )

    ordering = ('country',)


class AdventureAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'departure_date',
        'return_date',
        'slot',
        'image',
    )

    ordering = ('departure_date',)


admin.site.register(Adventure, AdventureAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(AdventureLocation, AdventureLocationAdmin)