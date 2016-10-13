# Create your models here.
# from __future__ import unicode_literals
from django.db import models
# Create your models here.
class Users(models.Model):
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    middlename = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    dateofB = models.CharField(max_length=45)

    class Meta:
        db_table = "person"
        # db_table = "career"

class Administrator(models.Model):
    num = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)

    class Meta:
        db_table = "administrator"
