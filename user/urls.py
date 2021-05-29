
from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.UserAPIView.as_view()),
    path('users/<int:id>/', views.UserAPIView.as_view()),
    path('signup/', views.SignupAPIView.as_view()),
    path('login/', views.UserLoginAPIView.as_view()),
    path('logout/', views.UserLogoutAPIView.as_view()),
    path('profile/', views.UserProfileAPIView.as_view()),
    path('update_location/', views.OnlineUserAPIVIEW.as_view()),
]
