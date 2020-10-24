from django.urls import path, include
from movies_rental import views
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'movies', views.MovieViewSet, basename='movies')

# The API URLs are now determined automatically by the router
urlpatterns = [
	path('', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)