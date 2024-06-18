from django.contrib.auth.models import User
from movies_rental.models import Movie,Like,Rental,Purchase
#from movies_rental.permissions import IsOwnerOrReadOnly
from movies_rental.serializers import MovieSerializer, MovieLikeSerializer, RentalSerializer, UserSerializer, PurchaseSerializer
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class MovieViewSet(viewsets.ModelViewSet):
	"""
	This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.

	"""
	#queryset = Movie.objects.all().order_by('title')
	serializer_class = MovieSerializer
	permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
	filterset_fields = ['availability']
	ordering_fields = ['title','likes']
	search_fields = ['title']

	def get_queryset(self):
		if self.request.user.is_staff:
			return Movie.objects.all().order_by('title')
		else:
			return Movie.objects.filter(availability=True).order_by('title')

	#	def get_serializer_class(self):
	#		if self.action == 'like':
	#			return MovieLikeSerializer
	#		else:
	#			return MovieSerializer

	@action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
	def like(self, request, *args, **kwargs):
		movie = self.get_object()

		if serializer.is_valid(): 
			if self.is_like_valid(movie, request.user):
				movie.likes = movie.likes + 1 if movie.likes else 1
				movie.save()
				Like.objects.create(user=request.user, movie=movie)
				return Response(serializer.data)
			else:
				return Response(status=status.HTTP_403_FORBIDDEN)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	@action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
	def unlike(self, request, *args, **kwargs):
		movie = self.get_object()
		serializer = MovieLikeSerializer(movie, data=request.data)
		if serializer.is_valid():
			if self.is_unlike_valid(movie, request.user):
				movie.likes = movie.likes - 1 if movie.likes else 0
				movie.save()
				Like.objects.filter(user=request.user, movie=movie).delete()
				return Response(serializer.data)
			else:
				return Response(status=status.HTTP_403_FORBIDDEN)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def is_like_valid(self, movie, user):
		if Like.objects.filter(movie=movie, user=user).count() != 0:
			return False #Este usuario ya dio like anteriormente a esta pelicula
		return True


	def is_unlike_valid(self, movie, user):
		if Like.objects.filter(movie=movie, user=user).count() == 0:
			return False #Este usuario no ha dado like anteriormente a esta pelicula
		return True


class RentalViewSet(viewsets.ModelViewSet):
	"""
	This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.

	"""
	queryset = Rental.objects.all().order_by('rental_date')
	serializer_class = RentalSerializer
	permission_classes = [permissions.IsAuthenticated]


class PurchaseViewSet(viewsets.ModelViewSet):
	"""
	This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.

	"""
	queryset = Purchase.objects.all().order_by('purchase_date')
	serializer_class = PurchaseSerializer
	permission_classes = [permissions.IsAuthenticated]


@ensure_csrf_cookie
def testView(request):
	
	return render(request, 'index.html',{})