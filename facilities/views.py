from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Facility
from .serializers import FacilitySerializer

# List all facilities or create a new one
class FacilityListCreateView(generics.ListCreateAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

# Retrieve, update, or delete a facility
class FacilityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

