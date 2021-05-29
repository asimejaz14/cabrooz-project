from django.utils import timezone
from django.db import models
from option.models import Option
from django.db.models import DO_NOTHING

# Create your models here.
from Cabrooz_App import settings


class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=200, null=True, blank=True)
    vehicle_number = models.CharField(unique=True, max_length=200, null=True, blank=True)
    vehicle_color = models.CharField(max_length=200, null=True, blank=True)
    vehicle_model = models.CharField(max_length=200, null=True, blank=True)
    vehicle_maker = models.CharField(max_length=200, null=True, blank=True)
    vehicle_category = models.ForeignKey(Option, related_name='vehicle_category_id', on_delete=DO_NOTHING, null=True, blank=True)
    driver = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True, related_name='driver_id', null=True, blank=True, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(Option, on_delete=DO_NOTHING, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vehicle_name

