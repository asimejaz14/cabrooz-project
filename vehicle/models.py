from django.db import models

# Create your models here.
from Cabrooz_App import settings


class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=200, null=True, blank=True)
    registration_number = models.CharField(unique=True, max_length=200, null=True, blank=True)
    vehicle_color = models.CharField(max_length=200, null=True, blank=True)
    vehicle_model = models.CharField(max_length=200, null=True, blank=True)
    vehicle_maker = models.CharField(max_length=200, null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.vehicle_name

