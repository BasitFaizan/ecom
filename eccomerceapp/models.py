from django.db import models

# Create your models here.
class users(models.Model):
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=30)
