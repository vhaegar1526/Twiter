from django.db import models

# Create your models here.
class Greet(models.Model):
    username = models.CharField(max_length=30)