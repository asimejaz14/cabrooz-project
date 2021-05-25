from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import (HTTP_401_UNAUTHORIZED,
                                   HTTP_500_INTERNAL_SERVER_ERROR,
                                   HTTP_404_NOT_FOUND,
                                   HTTP_201_CREATED,
                                   HTTP_200_OK,
                                   HTTP_400_BAD_REQUEST
                                   )

from user.models import User
from user.serializers import UserSerializer
from user.utils import create_message, get_default_param


class UserController:
    def get_user(self, request, id):
        try:
            sort_by = get_default_param(request, 'order_by', 'created_datetime')
            order = get_default_param(request, 'order', 'desc')

            if order == 'asc':
                pass
            else:
                sort_by = '-' + sort_by

            if id:
                try:
                    user = User.objects.get(id=id)
                    serialized_user = UserSerializer(user)
                    return Response(create_message(HTTP_200_OK, 'Success', serialized_user.data))
                except Exception as e:
                    print("USER LISTING EXCEPTION", e)
                    return Response(create_message(HTTP_404_NOT_FOUND, 'Error', 'User not found'))

            users = User.objects.filter(status=1).order_by(sort_by)
            serialized_user = UserSerializer(users, many=True)
            return Response(create_message(HTTP_200_OK, 'Success', serialized_user.data))
        except Exception as e:
            print("USER LISTING EXCEPTION", e)
            return Response(create_message(HTTP_404_NOT_FOUND, 'Error', 'User not found'))

    def create_user(self, request):
        try:
            if request.data.get('password'):
                request.POST._mutable = True
                request.data['password'] = make_password(request.data.get('password'))
                request.POST._mutable = False
            serialized_user = UserSerializer(data=request.data, context={'request': request})
            if serialized_user.is_valid():
                serialized_user.save()
                return Response(create_message(HTTP_201_CREATED, 'Success', serialized_user.data))
            else:
                print("User Not Added")

                print(serialized_user.errors)
                return Response(create_message(HTTP_400_BAD_REQUEST, 'Error', 'User not created'))
        except Exception as e:
            print("User Not Added", e)
            return Response(create_message(HTTP_400_BAD_REQUEST, 'Error', 'User not created'))

    def update_user(self, request, id):
        try:
            if request.data.get('password'):
                request.POST._mutable = True
                request.data['password'] = make_password(request.data.get('password'))
                request.POST._mutable = False

            user = User.objects.get(pk=id)
            serialized_user = UserSerializer(user, data=request.data, context={'request': request})
            if serialized_user.is_valid():
                serialized_user.save()
                return Response(create_message(HTTP_201_CREATED, 'Success', serialized_user.data))
            else:
                print("User Not Updated")
                print(serialized_user.errors)
                return Response(create_message(HTTP_400_BAD_REQUEST, 'Error', 'User not updated'))

        except Exception as e:
            print("User Not Updated", e)
            return Response(create_message(HTTP_400_BAD_REQUEST, 'Error', 'User not updated'))

    def delete_user(self, request):
        try:
            record_id = get_default_param(request, 'record_id', None)
            try:
                user = User.objects.get(pk=record_id)
                user.status = 2
                user.save()
                return Response(create_message(HTTP_200_OK, 'Success', 'User deleted'))
            except Exception as e:
                print("GET USER EXCEPTION", e)
                return Response(create_message(HTTP_400_BAD_REQUEST, 'Error', 'User not deleted'))
        except Exception as e:
            print("User Not Deleted", e)
            return Response(create_message(HTTP_400_BAD_REQUEST, 'Error', 'User not deleted'))
