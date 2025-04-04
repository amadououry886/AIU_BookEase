from rest_framework import serializers
from facilities.models import Facility

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'  # This includes all fields of the User model
