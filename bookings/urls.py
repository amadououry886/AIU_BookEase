from django.urls import path
from bookings.views import BookingListCreateView, BookingDetailView, CheckAvailabilityView

urlpatterns = [
    path('', BookingListCreateView.as_view(), name='booking-list'),
    path('<int:id>/', BookingDetailView.as_view(), name='booking-detail'),
    path('check-availability/', CheckAvailabilityView.as_view(), name='check-availability'),
]
