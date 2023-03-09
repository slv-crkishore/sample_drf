from django.db import models
from datetime import datetime, timedelta
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.


class UserModel(models.Model):
    name = models.CharField(max_length=100)
    username = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
