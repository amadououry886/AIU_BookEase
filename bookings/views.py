from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
from facilities.models import Facility

# ViewSet to handle CRUD operations for bookings
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# Custom view to check facility availability
class CheckAvailabilityView(APIView):
    def post(self, request):
        facility_id = request.data.get("facility_id")
        date = request.data.get("date")
        if not facility_id or not date:
            return Response({"error": "Missing parameters"}, status=400)
        
        facility = Facility.objects.filter(id=facility_id).first()
        if not facility:
            return Response({"error": "Facility not found"}, status=404)

        existing_booking = Booking.objects.filter(facility=facility, date=date).exists()
        if existing_booking:
            return Response({"available": False})
        return Response({"available": True})
