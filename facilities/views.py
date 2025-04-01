from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Facility
from .serializers import FacilitySerializer

class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


