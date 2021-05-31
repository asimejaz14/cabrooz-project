
from django.urls import path

from . import views
from .models import Ride

urlpatterns = [
    path('generate_ride_request/', views.RideAPIView.as_view()),
]
