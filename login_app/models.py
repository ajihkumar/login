
from django.db import models

'''
class add(models.Model):
    Address=models.BooleanField('is admin',default=False)
    is_staff=models.BooleanField('is admin',default=False)
    is_parent=models.BooleanField('is admin',default=False)


'''
gender_choices = (('MALE', 'MALE'), ('FEMALE', 'FEMALE'))
class datas(models.Model):
    Firstname = models.CharField(max_length=20,default="")
    Secondname = models.CharField(max_length=15,default="")
    mail = models.EmailField(max_length=50,default="")
    Dob = models.DateField(max_length=20,default="")
    Age = models.CharField(max_length=20,default="")
    Gender = models.CharField(max_length=6, choices=gender_choices)
    Address = models.CharField(max_length=150,default="")

    def __str__(self):
        return self.Firstname

# Create your models here.