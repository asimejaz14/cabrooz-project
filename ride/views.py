from django.shortcuts import render
from rest_framework.views import APIView

from .ride_controller import RideController

# Create your views here.
class RideAPIView(APIView):
    ride_controller_obj = RideController()

    def get(self, request):
        ...

    def post(self, request):
        return self.ride_controller_obj.generate_ride_request(request)