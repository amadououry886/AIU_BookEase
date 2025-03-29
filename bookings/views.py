from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Booking
from .serializers import BookingSerializer
from facilities.models import Facility
from datetime import datetime

# Create and list bookings
class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# Retrieve, update, or cancel a booking
class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# Check facility availability
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
