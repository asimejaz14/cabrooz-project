
from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.UserAPIView.as_view()),
    path('users/<int:id>', views.UserAPIView.as_view()),
    path('login/', views.UserLoginAPIView.as_view()),
]
