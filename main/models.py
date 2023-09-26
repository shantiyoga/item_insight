from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ItemStore(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()   
    price = models.BigIntegerField()
    category = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)