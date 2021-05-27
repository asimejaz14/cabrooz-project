
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import DO_NOTHING
from phonenumber_field.modelfields import PhoneNumberField

from option.models import Option


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    profile_image = models.ImageField(upload_to='user/profile_images/', blank=True, null=True)
    phone_number = PhoneNumberField(unique=True, max_length=200, null=True, blank=True)
    username = models.CharField(unique=True, max_length=200, null=True, blank=True)
    status = models.ForeignKey(Option, on_delete=DO_NOTHING, related_name='status_id', max_length=200, blank=True, null=True)
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
