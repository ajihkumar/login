
from django.shortcuts import redirect, render
from .forms import createuserform 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login

from.forms import  createuserform,LoginForm



def home(request):
    return render(request,'home.html')

def register(request):    
   if request.method=='POST':
        name=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]

        if password1==password2:        
            user=User.objects.create_user(username=name,email=email,password=password1)
            user.is_staff=True
            user.is_superuser=True
            user.save()
        
            messages.success(request,'Your account has been created! You are able to login')
            return redirect('signin')
        else:
            messages.warning(request,'Password Mismatching...!!!')
            return redirect('register')        
   else:
        form=createuserform()        
        return render(request,"register.html",{'form':form})
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            #messages.success(request, ' welcome our brightwheel !!')
            return redirect('signup')
        else:
            messages.info(request, 'account not exit plz register')
    form = LoginForm()
    return render(request,"signin.html",{'form':form})


 





     

def signup(request):
    return render(request,'signup.html')
def forgot(request):
    return render(request,'forgot-password.html')
def index(request):
    if request.method == 'POST':
        form=createuserform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your account has been created! You are able to login')
            return redirect('signin')
        else:
            messages.error(request,"something error,please correct fill the form") 
            return redirect('index')  

    



    form=createuserform()
    return render(request,'index.html',{'form':form})
    

# Create your views here.
