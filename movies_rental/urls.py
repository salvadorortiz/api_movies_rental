from django.urls import path, include
from movies_rental import views
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'movies', views.MovieViewSet, basename='movie')
router.register(r'rentals', views.RentalViewSet, basename='rental')
router.register(r'purchases', views.PurchaseViewSet, basename='purchase')

# The API URLs are now determined automatically by the router
urlpatterns = [
	path('', include(router.urls)),
	path('test/', views.testView),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)