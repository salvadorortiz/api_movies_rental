from django.urls import reverse
from django.test import Client
from rest_framework.test import APITestCase
from rest_framework.views import status

from movies_rental.models import Movie,Like,Rental,Purchase
from django.contrib.auth.models import User

class MovieListCreateAPIView(APITestCase):
	def setUp(self) -> None:
		self.url = reverse('movies-list', kwargs={})
		password = "123"
		self.user = User.objects.create_superuser(
					username = 'test',
					password = password
				)
		self.client = Client()
		self.client.login(username=self.user.username, password=password)
		
	def test_create_movie(self):
		self.assertEquals(
			Movie.objects.count(),
			0
		)

		data = {
			'title': 'test1',
			'description': 'test1'
		}

		response = self.client.post(self.url, data=data, format='json')
		
		self.assertEquals(
			response.status_code,
			status.HTTP_201_CREATED
		)
		
		self.assertEquals(
			Movie.objects.count(),
			1
		)

		movie = Movie.objects.first()

		self.assertEquals(
			movie.title,
			data['title']
		)

		self.assertEquals(
			movie.description,
			data['description']
		)

	def test_get_movie_list(self):
		movie = Movie.objects.create(
					title = 'test1',
					description = 'test1'
				)

		response = self.client.get(self.url)
		response_json = response.json()
		"""
		response_json =
		{'count': 1, 
		 'next': None, 
		 'previous': None, 
		 'results': [
		 			{'url': 'http://testserver/movies/2/', 'movie_id': 2, 'title': 'test1', 'description': 'test1', 'url_image': None, 'stock': 0, 'rental_price': '0.00', 'sale_price': '0.00', 'availability': False, 'likes': 0, 'likes_count': 0}
		 			]
		}
		"""

		self.assertEquals(
			response.status_code,
			status.HTTP_200_OK
		)

		self.assertEquals(
			response_json['count'],
			1
		)

		data = response_json['results'][0]

		self.assertEquals(
			data['title'],
			movie.title
		)

class MovieDetailsAPIViewTest(APITestCase):
	def setUp(self) -> None:
		self.movie = Movie.objects.create(title = 'test1', description = 'test1')
		self.url = reverse('movies-detail', kwargs={'pk': self.movie.pk})
#		password = "123"
#		self.user = User.objects.create_superuser(
#					username = 'test',
#					password = password
#				)
#		self.client = Client()
#		self.client.login(username=self.user.username, password=password)

	def test_get_movie_details(self):
		response = self.client.get(self.url)
		
		self.assertEquals(
			response.status_code,
			status.HTTP_200_OK
		)

		data = response.json()

		self.assertEquals(
			data['movie_id'],
			self.movie.pk
		)

		self.assertEquals(
			data['title'],
			self.movie.title
		)

		self.assertEquals(
			data['description'],
			self.movie.description
		)

	def test_update_movie(self):
		response = self.client.get(self.url)
		self.assertEquals(
			response.status_code,
			status.HTTP_200_OK
		)

		data = response.json()
		data['title'] = 'test2'
		data['description'] = 'test2'

		response = self.client.put(self.url, data=data, format="json")
		self.assertEquals(
			response.status_code,
			status.HTTP_200_OK
		)

		self.movie.refresh_from_db()

		self.assertEquals(
			data['title'],
			self.movie.title
		)

		self.assertEquals(
			data['description'],
			self.movie.description
		)