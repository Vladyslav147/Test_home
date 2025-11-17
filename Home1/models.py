from django.db import models

# Create your models here.
class UserProfile(models.Model): # Лучше назвать модель в соответствии с её целью
    name = models.CharField(max_length=100) # Вместо text
    phone = models.IntegerField() # Вместо number
    email = models.EmailField()
    