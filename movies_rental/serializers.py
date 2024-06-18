from rest_framework import serializers
from movies_rental.models import Movie,Like,Rental,Purchase
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class MovieSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name="movie-detail")
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

class RentalSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name="rental-detail")
	return_date = serializers.DateTimeField(format='%d-%m-%Y',input_formats=['%d-%m-%Y',])
	rental_date = serializers.DateTimeField(format='%d-%m-%Y',input_formats=['%d-%m-%Y',])
	#movies = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='movie-detail')
	#movies = MovieSerializer(read_only=True,many=True)

	class Meta:
		model = Rental
		fields = ['url','rental_date','return_date','user','movie','cost']
		#depth = 1 #for get more detail about of foreign key

class PurchaseSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name="purchase-detail")
	purchase_date = serializers.DateTimeField(format='%d-%m-%Y',input_formats=['%d-%m-%Y',])

	class Meta:
		model = Purchase
		fields = ['url','purchase_date','user','movie','cost']

