from django.db import models


# Create your models here.
class Option(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.key + '-' + self.value

    def natural_key(self):
        return self.key
