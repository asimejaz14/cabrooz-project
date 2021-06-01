
from django.urls import path

from . import views
from .models import Ride

urlpatterns = [
    path('generate_ride_request/', views.RideAPIView.as_view()),
    path('get_active_requests/', views.ActiveRideRequestAPIView.as_view()),
    path('update_ride_request/', views.RideRequestAPIView.as_view()),
]
