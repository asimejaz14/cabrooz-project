from django.db import models
from django.db.models import DO_NOTHING
from django.utils import timezone

# Create your models here.
from Cabrooz_App import settings
from option.models import Option


class Ride(models.Model):
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='ride_driver', null=True, blank=True, on_delete=DO_NOTHING)
    rider = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='ride_rider',  null=True, blank=True, on_delete=DO_NOTHING)
    estimated_fare = models.CharField(max_length=200, null=True, blank=True)
    actual_fare = models.CharField(max_length=200, null=True, blank=True)
    pick_up_location = models.CharField(max_length=200, null=True, blank=True)
    drop_off_location = models.CharField(max_length=200, null=True, blank=True)
    estimated_time = models.DurationField(max_length=200, null=True, blank=True)
    actual_time = models.DurationField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    started_datetime = models.DateTimeField(max_length=200, null=True, blank=True)
    ended_datetime = models.DateTimeField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    arrived_at_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    arrived_at_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    arrived_at_datetime = models.DateTimeField(max_length=200, null=True, blank=True)
    accepted_at_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    accepted_at_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    accepted_at_datetime = models.DateTimeField(max_length=200, null=True, blank=True)
    pick_up_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    pick_up_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    drop_off_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    drop_off_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    ride_status = models.ForeignKey(Option, on_delete=DO_NOTHING, related_name='ride_ride_status', null=True, blank=True)
    online_offline = models.ForeignKey(Option, null=True, blank=True, related_name='ride_online_offline', on_delete=DO_NOTHING)
    vehicle_category = models.ForeignKey(Option, null=True, blank=True, related_name='ride_vehicle_category', on_delete=DO_NOTHING)


class RideRequest(models.Model):
    rider = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='riderequest_rider', null=True, blank=True, on_delete=DO_NOTHING)
    estimated_fare = models.CharField(max_length=200, null=True, blank=True)
    pick_up_location = models.CharField(max_length=200, null=True, blank=True)
    drop_off_location = models.CharField(max_length=200, null=True, blank=True)
    estimated_time = models.DurationField(max_length=200, null=True, blank=True)
    pick_up_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    pick_up_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    drop_off_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    drop_off_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    ride_status = models.ForeignKey(Option, on_delete=DO_NOTHING, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expiry_time = models.DateTimeField(null=True, blank=True)
    online_offline = models.ForeignKey(Option, null=True, blank=True, related_name='riderequest_online_offline', on_delete=DO_NOTHING)
    vehicle_category = models.ForeignKey(Option, null=True, blank=True, related_name='riderequest_vehicle_category', on_delete=DO_NOTHING)
    is_alive = models.BooleanField(default=False, null=True, blank=True)
