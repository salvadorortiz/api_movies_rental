from django.contrib import admin
from movies_rental.models import Movie, Rental, Purchase

# Register your models here.
admin.site.register(Rental)
admin.site.register(Purchase)
