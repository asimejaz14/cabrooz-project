from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.status import (
                                   HTTP_404_NOT_FOUND,
                                   HTTP_201_CREATED,
                                   HTTP_200_OK,
                                   HTTP_400_BAD_REQUEST
                                   )

from user.models import User
from user.serializers import UserSerializer, UserProfileSerializer
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
                    user = User.objects.get(pk=id)
                    serialized_user = UserSerializer(user, context={'request': request})
                    return Response(create_message(HTTP_200_OK, 'Success', serialized_user.data))
                except Exception as e:
                    print("USER LISTING EXCEPTION", e)
                    return Response(create_message(HTTP_404_NOT_FOUND, 'Error', 'User not found'))

            users = User.objects.filter(status=1).order_by(sort_by)
            serialized_user = UserSerializer(users, context={'request': request}, many=True)
            return Response(create_message(HTTP_200_OK, 'Success', serialized_user.data))
        except Exception as e:
            print("USER LISTING EXCEPTION", e)
            return Response(create_message(HTTP_404_NOT_FOUND, 'Error', 'User not found'))


    def update_user(self, request, id):
        try:
            if request.data.get('password'):
                request.POST._mutable = True
                request.data['password'] = make_password(request.data.get('password'))
                request.POST._mutable = False

            user = User.objects.get(pk=id)
            serialized_user = UserSerializer(user, data=request.data, context={'request': request}, partial=True)
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


    def user_signup(self, request):
        try:
            request.POST._mutable = True
            request.data['status_id'] = 1
            request.data['password'] = make_password(request.data.get('password'))
            request.POST._mutable = False
            serialized_user = UserSerializer(data=request.data, context={'request': request})
            if serialized_user.is_valid():
                serialized_user.save()
                user = User.objects.get(email=request.data.get('email'))
                user.set_password(request.data.get('password'))
                user.save()
                return Response(create_message(HTTP_201_CREATED, 'Success', serialized_user.data))
            else:
                print("User Not Added")

                print(serialized_user.errors)
                return Response(create_message(HTTP_400_BAD_REQUEST, 'Error', 'User not created'))
        except Exception as e:
            print("User Not Added", e)
            return Response(create_message(HTTP_400_BAD_REQUEST, 'Error', 'User not created'))

    def user_logout(self, request):
        try:
            request.user.auth_token.delete()
            return Response(create_message(HTTP_200_OK, 'Success', 'User logged out successfully'))
        except Exception as e:
            print("USER LOGOUT EXCEPTION", e)
            return Response(create_message(HTTP_400_BAD_REQUEST, 'Error', 'User not logged out'))

    def get_user_profile(self, request):
        try:
            user = User.objects.get(email=request.user.email)
            serialized_user = UserProfileSerializer(user)

            return Response(create_message(HTTP_200_OK, 'Success', serialized_user.data))
        except Exception as e:
            print("USER PROFILE EXCEPTION", e)
            return Response(create_message(HTTP_400_BAD_REQUEST, 'Error', e))
