from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FacilityViewSet

# Create a router and register your viewset
router = DefaultRouter()
router.register(r'facilities', FacilityViewSet, basename='facility')

urlpatterns = [
    path('', include(router.urls)),  # This will generate all CRUD routes automatically
]
