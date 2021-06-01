from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.status import (
                                   HTTP_404_NOT_FOUND,
                                   HTTP_201_CREATED,
                                   HTTP_200_OK,
                                   HTTP_400_BAD_REQUEST,
                                   HTTP_500_INTERNAL_SERVER_ERROR
                                   )

from user.models import User, UserLiveLocation, OnlineUser
from user.serializers import (
    UserSerializer,
    UserProfileSerializer,
    UserLiveLocationSerializer,
    OnlineUserSerializer
    )
from Cabrooz_App.utils import create_message, get_default_param, get_distance


class UserController:
    def get_user(self, request, id):
        try:
            sort_by = get_default_param(request, 'order_by', 'created_datetime')
            order = get_default_param(request, 'order', 'desc')
            kwargs = {}

            if order == 'asc':
                pass
            else:
                sort_by = '-' + sort_by
            if id:
                kwargs['id'] = id

            users = User.objects.filter(**kwargs, status=1).order_by(sort_by)
            serialized_user = UserSerializer(users, context={'request': request}, many=True)
            return Response(create_message(HTTP_200_OK, 'Success', serialized_user.data))
        except Exception as e:
            print("USER LISTING EXCEPTION", e)
            return Response(create_message(HTTP_500_INTERNAL_SERVER_ERROR, 'Error', 'User not found'))


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
            return Response(create_message(HTTP_500_INTERNAL_SERVER_ERROR, 'Error', 'User not updated'))

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
            return Response(create_message(HTTP_500_INTERNAL_SERVER_ERROR, 'Error', 'User not deleted'))


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
            return Response(create_message(HTTP_500_INTERNAL_SERVER_ERROR, 'Error', 'User not created'))

    def user_logout(self, request):
        try:
            request.user.auth_token.delete()
            return Response(create_message(HTTP_200_OK, 'Success', 'User logged out successfully'))
        except Exception as e:
            print("USER LOGOUT EXCEPTION", e)
            return Response(create_message(HTTP_500_INTERNAL_SERVER_ERROR, 'Error', 'User not logged out'))

    def get_user_profile(self, request):
        try:
            user = User.objects.get(email=request.user.email)
            serialized_user = UserProfileSerializer(user)

            return Response(create_message(HTTP_200_OK, 'Success', serialized_user.data))
        except Exception as e:
            print("USER PROFILE EXCEPTION", e)
            return Response(create_message(HTTP_500_INTERNAL_SERVER_ERROR, 'Error', e))

    def update_user_location(self, request):
        try:
            request.POST._META = True
            user_id = request.data.get('user')
            longitude = request.data.get('current_longitude')
            latitude = request.data.get('current_latitude')
            user = UserLiveLocation.objects.filter(user_id=user_id).last()
            if user:
                try:
                    distance = get_distance(latitude, longitude, user.current_latitude, user.current_longitude)
                except Exception as e:
                    distance = 0
                    print("DISTANCE CALCULATION EXCEPTION", e)
                request.data['distance'] = distance
                request.POST._mutable = False
                serialized_online_user = UserLiveLocationSerializer(data=request.data)
                if serialized_online_user.is_valid():
                    serialized_online_user.save()
                    return Response(create_message(HTTP_201_CREATED, 'Success', serialized_online_user.data))
                else:
                    raise Exception
            request.data['distance'] = 0
            request.POST._mutable = False
            serialized_online_user = UserLiveLocationSerializer(data=request.data)
            if serialized_online_user.is_valid():
                serialized_online_user.save()
                return Response(create_message(HTTP_201_CREATED, 'Success', serialized_online_user.data))
            else:
                print(serialized_online_user.errors)
                raise Exception
        except Exception as e:
            print("USER UPDATE LOCATION EXCEPTION", e)
            return Response(create_message(HTTP_500_INTERNAL_SERVER_ERROR, 'Error', e))

    def update_online_user(self, request):
        try:
            user_id = request.data.get('user')
            try:
                user = OnlineUser.objects.get(user_id=user_id)
                serialized_user = OnlineUserSerializer(user, data=request.data, partial=True)
                if serialized_user.is_valid():
                    serialized_user.save()
                    return Response(create_message(HTTP_201_CREATED, 'Success', "User location updated"))
                else:
                    print("USER LOCATION EXISTS BUT ERROR IN UPDATE")
                    print(serialized_user.errors)
                    return Response(create_message(HTTP_400_BAD_REQUEST, 'Error', "User location not updated"))
            except:
                serialized_user = OnlineUserSerializer(data=request.data)
                if serialized_user.is_valid():
                    serialized_user.save()
                    return Response(create_message(HTTP_200_OK, 'Success', "User location updated"))
                else:
                    print("USER LOCATION CREATED ERROR")
                    print(serialized_user.errors)
                    return Response(create_message(HTTP_400_BAD_REQUEST, 'Error', "User location not updated"))

        except Exception as e:
            print("UPDATE ONLINE USER EXCEPTION", e)
            return Response(create_message(HTTP_500_INTERNAL_SERVER_ERROR, 'Error', e))