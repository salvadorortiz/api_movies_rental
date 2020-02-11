from rest_framework import serializers
from movies_rental.models import Movie,Rental,Purchase
from django.contrib.auth.models import User


class MovieSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Movie
		fields = ['url','movie_id','title','description','url_image','stock','rental_price','sale_price','availability','likes']


class MovieNonAdminSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Movie
		fields = ['likes']


