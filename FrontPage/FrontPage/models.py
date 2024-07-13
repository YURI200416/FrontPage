from django.db import models
from django.contrib.auth.models import User

class M(models.Model):
    model_image = models.ImageField(default = "pingpongscreen.JPG")