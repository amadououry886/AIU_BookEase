from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet, CheckAvailabilityView

# Create a router and register your viewset for Booking
router = DefaultRouter()
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('', include(router.urls)),  # Automatically generates CRUD endpoints for bookings
    path('check-availability/', CheckAvailabilityView.as_view(), name='check-availability'),  # Custom availability check
]
