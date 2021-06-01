from rest_framework.response import Response
from rest_framework.status import (
                                   HTTP_404_NOT_FOUND,
                                   HTTP_201_CREATED,
                                   HTTP_200_OK,
                                   HTTP_400_BAD_REQUEST,
                                   HTTP_500_INTERNAL_SERVER_ERROR
                                   )

from Cabrooz_App.utils import create_message, get_default_param
from .models import Vehicle
from .serializers import VehicleSerializer


class VehicleController:

    def get_vehicle_record(self, request, id):
        try:
            kwargs = {}
            if id:
                kwargs['id'] = id

            vehicles = Vehicle.objects.filter(**kwargs, status=1)
            serialized_vehicles = VehicleSerializer(vehicles, many=True)
            return Response(create_message(HTTP_200_OK, 'Success', serialized_vehicles.data))
        except Exception as e:
            print("VEHICLE NOT FOUND EXCEPTION", e)
            return Response(create_message(HTTP_400_BAD_REQUEST, 'Error', "Vehicle record not found."))

    def create_vehicle_record(self, request):
        try:
            request.POST._mutable = True
            request.data['status'] = 1
            request.POST._mutable = False

            serialized_vehicle = VehicleSerializer(data=request.data)

            if serialized_vehicle.is_valid():
                serialized_vehicle.save()
                return Response(create_message(HTTP_201_CREATED, 'Success', "Vehicle record created."))
            else:
                print(serialized_vehicle.errors)
                return Response(create_message(HTTP_400_BAD_REQUEST, 'Error', "Vehicle record not created."))

        except Exception as e:
            print("VEHICLE NOT ADDED EXCEPTION", e)
            return Response(create_message(HTTP_500_INTERNAL_SERVER_ERROR, 'Error', "Vehicle record not created."))

    def update_vehicle_record(self, request, id):
        try:
            if not id:
                return Response(create_message(HTTP_400_BAD_REQUEST, 'Error', "No record selected"))
            vehicle_obj = Vehicle.objects.get(pk=id)
            serialized_vehicle = VehicleSerializer(vehicle_obj, data=request.data, partial=True)

            if serialized_vehicle.is_valid():
                serialized_vehicle.save()
                return Response(create_message(HTTP_201_CREATED, 'Success', "Vehicle record updated."))
            else:
                print(serialized_vehicle.errors)
                return Response(create_message(HTTP_400_BAD_REQUEST, 'Error', "Vehicle record not updated."))
        except Exception as e:
            print("VEHICLE NOT UPDATED EXCEPTION", e)
            return Response(create_message(HTTP_500_INTERNAL_SERVER_ERROR, 'Error', "Vehicle record not updated."))

    def delete_vehicle_record(self, request):
        try:
            record_id = get_default_param(request, 'id', None)
            if not record_id:
                return Response(create_message(HTTP_400_BAD_REQUEST, 'Error', "Vehicle record not selected."))

            vehicle_record = Vehicle.objects.get(pk=record_id)
            vehicle_record.status = 2
            vehicle_record.save()
            return Response(create_message(HTTP_200_OK, 'Success', "Vehicle record deleted."))
        except Exception as e:
            print("VEHICLE NOT UPDATED EXCEPTION", e)
            return Response(create_message(HTTP_500_INTERNAL_SERVER_ERROR, 'Error', "Vehicle record not deleted."))