from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import DO_NOTHING
from phonenumber_field.modelfields import PhoneNumberField

from option.models import Option

# Create your models here.
from vehicle.models import Vehicle


class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    profile_image = models.ImageField(upload_to='user/profile_images/', blank=True, null=True)
    phone_number = PhoneNumberField(unique=True, max_length=200, null=True, blank=True)
    username = models.CharField(unique=True, max_length=200, null=True, blank=True)
    status = models.ForeignKey(Option, on_delete=DO_NOTHING, related_name='status_id', max_length=200, blank=True,
                               null=True)
    created_datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_datetime = models.DateTimeField(auto_now=True, null=True, blank=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    type = models.ForeignKey(Option, on_delete=DO_NOTHING, related_name='type_id', null=True, blank=True)
    cnic_front = models.ImageField(upload_to='user/documents/', blank=True, null=True)
    cnic_back = models.ImageField(upload_to='user/documents/', blank=True, null=True)
    license_front = models.ImageField(upload_to='user/documents/', blank=True, null=True)
    license_back = models.ImageField(upload_to='user/documents/', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)

    def save(self, *args, **kwargs):
        self.username = self.email
        super(User, self).save(*args, **kwargs)


class UserWallet(models.Model):
    user = models.ForeignKey(User, on_delete=DO_NOTHING, null=True, blank=True)
    amount = models.FloatField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name + " " + self.amount


class UserLiveLocation(models.Model):
    user = models.ForeignKey(User, on_delete=DO_NOTHING, blank=True, null=True)
    is_online = models.BooleanField(max_length=200, default=False, blank=True, null=True)
    current_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    current_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    distance = models.CharField(max_length=200, null=True, blank=True)
    type = models.ForeignKey(Option, null=True, blank=True, on_delete=DO_NOTHING)
    country = models.CharField(max_length=200, null=True, blank=True)
    on_ride = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.user.name


class OnlineUser(models.Model):
    user = models.OneToOneField(User, on_delete=DO_NOTHING, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    type = models.ForeignKey(Option, null=True, blank=True, on_delete=DO_NOTHING)
    is_online = models.BooleanField(default=False, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    on_ride = models.BooleanField(default=False, null=True, blank=True)


    def __str__(self):
        return self.user.first_name

