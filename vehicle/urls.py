from django.urls import path

from . import views


urlpatterns = [
    path('vehicles/', views.VehicleAPIView.as_view()),
    path('vehicles/<int:id>/', views.VehicleAPIView.as_view()),
]
