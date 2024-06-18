# -*- coding: utf-8 -*-

from django.db import models
from auditlog.registry import auditlog


class Movie(models.Model):
	movie_id = models.AutoField(primary_key=True)
	title = models.CharField('Title',max_length=200)
	description = models.TextField('Description', blank=True, null=True)
	url_image = models.ImageField(upload_to="movie_images/", null=True, blank=True)
	stock = models.PositiveSmallIntegerField('Stock', null=True, blank=True)
	rental_price = models.DecimalField('Rental price', max_digits=6, decimal_places=2, default=0.0,null=True, blank=True)
	sale_price = models.DecimalField('Sale price', max_digits=6, decimal_places=2, default=0.0,null=True, blank=True)
	availability = models.BooleanField('Availability', default=True)
	likes = models.PositiveSmallIntegerField('Likes', null=True, blank=True)
	
	def __str__(self):
		return self.title

auditlog.register(Movie, include_fields=['title','rental_price','sale_price'])

class Like(models.Model):
	movie = models.ForeignKey('Movie', related_name='like_movie', on_delete=models.CASCADE)
	user = models.ForeignKey('auth.User', related_name='like_user', on_delete=models.CASCADE)


class Rental(models.Model):
	rental_id = models.AutoField(primary_key=True)
	rental_date = models.DateTimeField('Rental date', auto_now_add=True, null=True,blank=True)
	return_date = models.DateTimeField('Return date', auto_now_add=False, null=True,blank=True)
	user = models.ForeignKey('auth.User', related_name='rental_user', on_delete=models.CASCADE)
	movie = models.ForeignKey('Movie', related_name='rental_movie', on_delete=models.CASCADE)
	cost = models.DecimalField('Cost', max_digits=6, decimal_places=2, default=0.0,null=True, blank=True)
	

class Purchase(models.Model):
	purchase_id = models.AutoField(primary_key=True)
	purchase_date = models.DateTimeField('Rental date', auto_now_add=True, null=True,blank=True)
	user = models.ForeignKey('auth.User', related_name="purchase_user", on_delete=models.CASCADE)
	movie = models.ForeignKey('Movie', related_name='purchase_movie', on_delete=models.CASCADE)
	cost = models.DecimalField('Cost', max_digits=6, decimal_places=2, default=0.0,null=True, blank=True)




	