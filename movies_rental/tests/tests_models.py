from django.test import TestCase
from movies_rental.models import Movie,Like,Rental,Purchase
from django.contrib.auth.models import User

class MovieTestCase(TestCase):

	def test_movie(self):
		self.assertEquals(
			Movie.objects.count(),
			0
		)

		Movie.objects.create(
			title = 'test1',
			description = 'test1',
			url_image = '',
			stock = 0,
			rental_price = 0.0,
			sale_price = 0.0,
			availability = False,
			likes = 0
		)

		Movie.objects.create(
			title = 'test2',
			description = 'test2',
			url_image = '',
			stock = 1,
			rental_price = 1.0,
			sale_price = 2.0,
			availability = True,
			likes = 1
		)

		self.assertEquals(
			Movie.objects.count(),
			2
		)

		available_movies = Movie.objects.filter(availability = True)

		self.assertEquals(
			available_movies.count(),
			1
		)

class LikeTestCase(TestCase):

	def test_like(self):
		self.assertEquals(
			Like.objects.count(),
			0
		)

		movie = Movie.objects.create(
					title = 'test1',
					description = 'test1',
					url_image = '',
					stock = 0,
					rental_price = 0.0,
					sale_price = 0.0,
					availability = False,
					likes = 0
				)

		user = User.objects.create(
					username = 'test',
					password = '123',
					email = "test@test.com",
					first_name = 'test',
					last_name = 'test'
				)

		Like.objects.create(
			movie = movie,
			user = user
		)

		self.assertEquals(
			Like.objects.count(),
			1
		)

class RentalTestCase(TestCase):

	def test_rental(self):
		self.assertEquals(
			Rental.objects.count(),
			0
		) 

		movie = Movie.objects.create(
					title = 'test1',
					description = 'test1',
					url_image = '',
					stock = 0,
					rental_price = 0.0,
					sale_price = 0.0,
					availability = False,
					likes = 0
				)

		user = User.objects.create(
					username = 'test',
					password = '123',
					email = "test@test.com",
					first_name = 'test',
					last_name = 'test'
				)

		Rental.objects.create(
			user = user,
			movie = movie
		)

		self.assertEquals(
			Rental.objects.count(),
			1
		)

class PurchaseTestCase(TestCase):

	def test_purchase(self):
		self.assertEquals(
			Purchase.objects.count(),
			0
		) 

		movie = Movie.objects.create(
					title = 'test1',
					description = 'test1',
					url_image = '',
					stock = 0,
					rental_price = 0.0,
					sale_price = 0.0,
					availability = False,
					likes = 0
				)

		user = User.objects.create(
					username = 'test',
					password = '123',
					email = "test@test.com",
					first_name = 'test',
					last_name = 'test'
				)

		Purchase.objects.create(
			user = user,
			movie = movie
		)

		self.assertEquals(
			Purchase.objects.count(),
			1
		)
