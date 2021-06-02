from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model


# Create your models here.


class Profile(Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


class Trail(Model):

    trail_name = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    length = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=50)
    favorited = models.ManyToManyField(Profile)


class CommunityHike(Model):

    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="community_hikes")
    trail = models.ForeignKey(Trail, on_delete=models.CASCADE, related_name="community_hikes")
    date = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    attendees = models.ManyToManyField(Profile)