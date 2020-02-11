from django.contrib.auth.models import User
from movies_rental.models import Movie,Rental,Purchase
#from movies_rental.permissions import IsOwnerOrReadOnly
from movies_rental.serializers import MovieSerializer, MovieNonAdminSerializer#, UserSerializer
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class MovieViewSet(viewsets.ModelViewSet):
	"""
	This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.

	"""
	queryset = Movie.objects.all().order_by('title')
	serializer_class = MovieSerializer
	permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
	filterset_fields = ['availability']
	ordering_fields = ['title','likes']

#	def get_serializer_class(self):
#		if self.action == 'like':
#			return MovieNonAdminSerializer
#		else:
#			return MovieSerializer
#
#			return Response(serializer.data)

	@action(detail=True, methods=['put','patch'], permission_classes=[permissions.IsAuthenticated])
	def like(self, request, *args, **kwargs):
		movie = self.get_object()
		serializer = MovieNonAdminSerializer(movie, data=request.data)
		if serializer.is_valid():
			movie.likes = movie.likes + 1 if movie.likes else 1 #VALIDAR QUE YA TIENE LIKE
			movie.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



	@action(detail=True, methods=['put','patch'], permission_classes=[permissions.IsAuthenticated])
	def unlike(self, request, *args, **kwargs):
		movie = self.get_object()
		serializer = MovieNonAdminSerializer(movie, data=request.data)
		if serializer.is_valid():
			movie.likes = movie.likes - 1 if movie.likes else 0 #VALIDAR QUE YA TIENE LIKE
			movie.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
