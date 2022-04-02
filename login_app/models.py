from email.headerregistry import Address
from operator import concat
from unicodedata import name
from django.db import models



class datas(models.Model):
    name = models.CharField(max_length=20,default="")
    age = models.IntegerField(max_length=10,default="")
    Address = models.CharField(max_length=50,default="")
    concat = models.IntegerField(max_length=20,default="")
    mail = models.CharField(max_length=20,default="")

# Create your models here.
