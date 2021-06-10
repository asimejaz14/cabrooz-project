from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .ride_controller import RideController


# Create your views here.
class RideAPIView(APIView):
    permission_classes = [IsAuthenticated]
    ride_controller_obj = RideController()

    def get(self, request):
        return self.ride_controller_obj.get_ride_request(request)

    def post(self, request):
        return self.ride_controller_obj.create_ride_request(request)


class ActiveRideRequestAPIView(APIView):
    permission_classes = [IsAuthenticated]
    ride_controller_obj = RideController()

    def get(self, request):
        return self.ride_controller_obj.get_active_ride_requests(request)


class RideRequestAPIView(APIView):
    permission_classes = [IsAuthenticated]
    ride_controller_obj = RideController()

    def patch(self, request):
        return self.ride_controller_obj.update_ride_request(request, id=None)
