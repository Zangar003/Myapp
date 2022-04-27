from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Person(models.Model):
    id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
