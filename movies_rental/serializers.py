from rest_framework import serializers
from movies_rental.models import Movie,Like,Rental,Purchase
from django.contrib.auth.models import User


class MovieSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name="movies-detail")
	likes_count = serializers.SerializerMethodField()

	class Meta:
		model = Movie
		fields = ['url','movie_id','title','description','url_image','stock','rental_price','sale_price','availability','likes', 'likes_count']

	def get_likes_count(self, obj):
		return Like.objects.filter(movie_id=obj.movie_id).count()

class MovieLikeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Movie
		fields = ['likes']


