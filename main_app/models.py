from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model

# Create your models here.


class Profile(Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
