from decimal import Decimal

from rest_framework.response import Response
from rest_framework.status import (
HTTP_200_OK,
HTTP_400_BAD_REQUEST,
HTTP_201_CREATED,
HTTP_404_NOT_FOUND,
)

from operator import itemgetter

from Cabrooz_App.utils import create_message, get_distance
from Cabrooz_App import enums
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

    def generate_ride_request(self, request):
        try:
            # drivers_distances = self.get_online_drivers_distance(request)
            # drivers_distances.sort(key=itemgetter(1))
            # for d in drivers_distances:
            #     print(d)
            # serialized_drivers = UserProfileSerializer(drivers_distances, many=True)
            # return Response(create_message(HTTP_200_OK, 'Success', serialized_drivers.data))
            return Response(create_message(HTTP_200_OK, 'Success', {}))

        except Exception as e:
            print("RIDE REQUEST EXCEPTION", e)
            return Response(create_message(HTTP_400_BAD_REQUEST, 'Error', e))