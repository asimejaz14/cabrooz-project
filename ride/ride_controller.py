from decimal import Decimal

from rest_framework.response import Response
from rest_framework.status import (
HTTP_200_OK,
HTTP_400_BAD_REQUEST,
HTTP_201_CREATED,
HTTP_404_NOT_FOUND,
HTTP_500_INTERNAL_SERVER_ERROR
)

from operator import itemgetter
from django.utils import timezone

from Cabrooz_App.utils import create_message, get_distance
from Cabrooz_App import enums
from ride.serializers import RideRequestSerializer
from user.models import OnlineUser, User
from user.serializers import UserProfileSerializer


class RideController:

    def get_online_drivers_distance(self, request):
        try:
            rider_pick_up_latitude = Decimal(request.data.get('pick_up_latitude'))
            rider_pick_up_longitude = Decimal(request.data.get('pick_up_latitude'))
            rider_drop_off_latitude = Decimal(request.data.get('drop_off_longitude'))
            rider_drop_off_longitude = Decimal(request.data.get('drop_off_longitude'))
            estimated_fare = Decimal(request.data.get('estimated_fare'))
            estimated_time = Decimal(request.data.get('estimated_time'))
            country = request.data.get('country')

            online_users = OnlineUser.objects.filter(is_online=True, type_id=enums.DRIVER, country=country)
            drivers_distances = []
            for online_user in online_users:
                drivers_distances.append([online_user, get_distance(online_user.latitude, online_user.longitude, rider_pick_up_latitude, rider_pick_up_longitude)])
            return drivers_distances
        except Exception as e:
            print("NEAREST DRIVER EXCEPTION", e)


    def get_ride_request(self, request):
        try:
            ...
        except Exception as e:
            print("GET RIDE REQUEST EXCEPTION", e)
            return Response(create_message(HTTP_500_INTERNAL_SERVER_ERROR, 'Error', e))


    def create_ride_request(self, request):
        try:
            # drivers_distances = self.get_online_drivers_distance(request)
            # drivers_distances.sort(key=itemgetter(1))
            # for d in drivers_distances:
            #     print(d)
            # serialized_drivers = UserProfileSerializer(drivers_distances, many=True)
            # return Response(create_message(HTTP_200_OK, 'Success', serialized_drivers.data))
            request.POST._mutable = True
            request.data['created_at'] = timezone.now()
            request.data['expiry_time'] = request.data['created_at'].replace(minute=request.data['created_at'].minute + 1)
            request.POST._mutable = False
            serialized_ride_request = RideRequestSerializer(data=request.data)
            if serialized_ride_request.is_valid():
                serialized_ride_request.save()
                return Response(create_message(HTTP_201_CREATED, 'Success', "Ride Request Created"))
            else:
                print(serialized_ride_request.errors)
            return Response(create_message(HTTP_400_BAD_REQUEST, 'Error', serialized_ride_request.errors))

        except Exception as e:
            print("RIDE REQUEST EXCEPTION", e)
            return Response(create_message(HTTP_500_INTERNAL_SERVER_ERROR, 'Error', e))