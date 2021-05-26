from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView


# Create your views here.
from .user_controller import UserController
from user.utils import create_message


class UserAPIView(APIView):
    permission_classes = [IsAuthenticated]
    user_controller_obj = UserController()


    def get(self, request, id=None):
        return self.user_controller_obj.get_user(request, id)

    def post(self, request):
        return self.user_controller_obj.create_user(request)

    def patch(self, request, id=None):
        return self.user_controller_obj.update_user(request, id)

    def delete(self, request):
        return self.user_controller_obj.delete_user(request)


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny,]

    def post(self, request):
        try:
            email_ = request.data.get('email')
            password_ = request.data.get('password')
            user = authenticate(email=email_, password=password_)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                if created:
                    token_ = Token.objects.get(user=user)
                    return Response(create_message(HTTP_201_CREATED, 'Success', str(token_)))
                elif token:
                    return Response(create_message(HTTP_201_CREATED, 'Success', str(token)))
        except Exception as e:
            print("USER LOGIN EXCEPTION", e)
            return Response(create_message(HTTP_400_BAD_REQUEST, 'Error', 'Invalid email/password'))


class SignupAPIView(APIView):
    permission_classes = [AllowAny,]
    user_controller_obj = UserController()

    def post(self, request):
        return self.user_controller_obj.user_signup(request)


class UserLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]
    user_controller_obj = UserController()

    def post(self, request):
        return self.user_controller_obj.user_logout(request)