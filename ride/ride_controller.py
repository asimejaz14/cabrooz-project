from rest_framework.response import Response
from rest_framework.status import (
HTTP_200_OK,
HTTP_400_BAD_REQUEST,
HTTP_201_CREATED,
HTTP_404_NOT_FOUND,
)

from Cabrooz_App.utils import create_message


class RideController:

    def generate_ride_request(self, request):
        try:
            ...
        except Exception as e:
            print("RIDE REQUEST EXCEPTION", e)
            return Response(create_message(HTTP_400_BAD_REQUEST, 'Error', e))