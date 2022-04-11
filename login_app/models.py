
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
    Dob = models.DateField(max_length=20)
    Age = models.CharField(max_length=20,default="")
    Gender = models.CharField(max_length=6, choices=gender_choices)
    Address = models.CharField(max_length=150,default="")

    def __str__(self):
        return self.Firstname


class createparents(models.Model):
    firstname = models.CharField(max_length=20,default="")
    secondname = models.CharField(max_length=15,default="")
    username = models.CharField(max_length=15,default="")
    mail = models.EmailField(max_length=50,default="")
    address = models.CharField(max_length=150,default="")
    password = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class createparentss(models.Model):
    firstname = models.CharField(max_length=20,default="")
    secondname = models.CharField(max_length=15,default="")
    username = models.CharField(max_length=15,default="")
    mail = models.EmailField(max_length=50,default="")
    address = models.CharField(max_length=150,default="")
    password = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return self.username


   


# Create your models here.