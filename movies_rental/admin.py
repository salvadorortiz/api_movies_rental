from django.contrib import admin
from movies_rental.models import Movie, Rental, Purchase

#admin.site.register(Rental)
#admin.site.register(Purchase)

from django.contrib import admin
from .models import Movie, Like, Rental, Purchase

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'stock', 'rental_price', 'sale_price', 'availability', 'likes')
    search_fields = ('title',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user')
    search_fields = ('movie__title', 'user__username')

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('rental_id', 'rental_date', 'return_date', 'user', 'movie', 'cost')
    search_fields = ('user__username', 'movie__title')

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('purchase_id', 'purchase_date', 'user', 'movie', 'cost')
    search_fields = ('user__username', 'movie__title')
