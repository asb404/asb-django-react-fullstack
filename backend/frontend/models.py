from django.db import models
import uuid
import MySQLdb
from django.contrib.auth.models import User
# Create your models here.

class users(models.Model):
    username=models.CharField(max_length=255,primary_key=True)
    email=models.CharField(max_length=255)
    pwd=models.CharField(max_length=255)
    def __str__(self):
        return self.username
    class Meta:
        db_table='users'


    