from rest_framework import serializers

from .models import RideRequest, Ride


class RideRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideRequest
        fields = '__all__'

