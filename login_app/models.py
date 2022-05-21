
from multiprocessing.sharedctypes import Value
from django.contrib.auth.models import AbstractBaseUser,User
from optparse import Option
from django.db import models
gender_choices = (('MALE', 'MALE'), ('FEMALE', 'FEMALE'))
class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    status_choice = (
        ('active', 'Active'),
        ('in_active', 'In_Active'),
        ('waitlist', 'Waitlist'),
        ('prospects', 'Prospects'),
        ('toured', 'Toured'),
        ('applied', 'Applied'),
    )
    status = models.CharField(choices=status_choice, max_length=10,)
    parentname=models.CharField(max_length=20)
    Dob = models.DateField(max_length=20)
    Age = models.CharField(max_length=2,default="")
    Gender = models.CharField(max_length=6, choices=gender_choices)
    #roll = models.CharField(max_length=10)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=10,null=True)
    #fee=models.PositiveIntegerField(null=True)
    #cl= models.CharField(max_length=10,choices=classes,default='one')
    #status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


class upload_image(models.Model):
    sender =models.ForeignKey(User,related_name= "sender",on_delete = models.CASCADE,null =True)
    receiver = models.ForeignKey(StudentExtra,related_name= "receiver",on_delete = models.CASCADE,null =True)
    image = models.ImageField(upload_to='upload_image/')
    
    def __str__(self):
        return "uploadimage"










class TeacherExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #salary = models.PositiveIntegerField(null=False)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=12)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name



class CustomUser(AbstractBaseUser):
    #user_type_data = ((1, "admin"), (2, "Staff"), (3, "parent"))
    #user_type = models.CharField(default="", choices=user_type_data, max_length=10)
    #id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    date_joined=models.DateTimeField(verbose_name='datejoined',auto_now_add=True)
    address= models.CharField( max_length=150, blank=True)
    last_login= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin= models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    status_choice = (
        ('active', 'Active'),
        ('in_active', 'In_Active'),
        ('waitlist', 'Waitlist'),
        ('prospects', 'Prospects'),
        ('toured', 'Toured'),
        ('applied', 'Applied'),
    )
    status = models.CharField(choices=status_choice, max_length=10,)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = models.Manager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


#class parent_schedule(models.Model):
 #   name=models.ForeignKey(StudentExtra,on_delete = models.CASCADE,null =True)




























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
    password = models.CharField(blank=False,max_length=10)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class createparentss(models.Model):
    firstname = models.CharField(max_length=20,default="")
    secondname = models.CharField(max_length=15,default="")
    username = models.CharField(max_length=15,default="")
    mail = models.EmailField(max_length=50,default="")
    address = models.CharField(max_length=150,default="")
    password = models.CharField(blank=False,max_length=10)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class createstaffs(models.Model):
    firstname = models.CharField(max_length=20,default="")
    secondname = models.CharField(max_length=15,default="")
    username = models.CharField(max_length=15,default="")
    mail = models.EmailField(max_length=50,default="")
    address = models.CharField(max_length=150,default="")
    password = models.CharField(blank=False,max_length=100)
    zip_code = models.CharField(max_length=20)

    
    def __str__(self):
        return self.username



   


# Create your models here.