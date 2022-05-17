
from django.shortcuts import redirect, render
#from login_app.decorator import unauthenticated_user, allowed_user


from .forms import createuserform 
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required,user_passes_test
from login import settings
from django.core.mail import send_mail
from login_app.helper import send_forget_password_mail


from.forms import  createuserform1
from login_app import forms, models



def home(request):
    return render(request,'signup.html')
  
    
   
def register(request):
    form=forms.AdminSigupForm()
    if request.method=='POST':
        form=forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()


            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            messages.success(request, "Registration successful." )
            return redirect("adminsignin")
        messages.error(request, "Unsuccessful registration. Invalid information.")
  
    return render (request=request, template_name="register.html", context={"form":form})


def teacher_signup_view(request):
    form =createuserform()
    form1 =forms.TeacherExtraForm()
    mydict={'form':form,'form1':form1}
    if request.method == 'POST':
        form =createuserform(request.POST, request.FILES)
        form1 =forms.TeacherExtraForm(request.POST, request.FILES)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()

            f2=form1.save(commit=False)
            f2.user=user
            user2=f2.save()

            my_teacher_group = Group.objects.get_or_create(name='STAFF')
            my_teacher_group[0].user_set.add(user)

        #messages.success(request, "Registration successful." )
        return redirect("teacherlogin")
        messages.error(request, "Unsuccessful registration. Invalid information.")
     
    return render(request=request, template_name='staff_register.html', context=mydict)
      
    form1=forms.createuserform()
    form2=forms.TeacherExtraForm()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.createuserform(request.POST)
        form2=forms.TeacherExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.user=user
            user2=f2.save()

            my_teacher_group = Group.objects.get_or_create(name='TEACHER')
            my_teacher_group[0].user_set.add(user)

        return redirect('teacherlogin')
    return render(request,'school/teachersignup.html',context=mydict)

def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_teacher(user):
    
    return user.groups.filter(name='STAFF').exists()


def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('superadmin')
    elif is_teacher(request.user):
        accountapproval=models.TeacherExtra.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('signup')
        else:
            return render(request,'main/staff_wait.html')
    

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)

def signin(request):
    if request.method == 'POST':
        name=request.POST['username']
        password1=request.POST['password1']
        user = authenticate(request, username = name, password=password1)
        if user is not None and user.is_staff==True and user.is_superuser==True:
            form = login(request, user)
            return redirect('superadmin')
        elif user is not None and user.is_staff==True and user.is_superuser==False:
            form = login(request, user)
            return redirect('staff') 
        elif user is not None:
            form = login(request, user)
            return redirect('parents')             
        else:  
            messages.warning(request,'account not exit...!!!')
            return redirect('signin')         
    form = createuserform ()
    return render(request,"signin.html",{'form':form})

def signup(request):
    return render(request,'signup.html')
import uuid
  
def forgot(request):
    try:
        if request.method == 'POST':
            name=request.POST.get('username') 

            if not User.objects.filter(username=name).first(): 
                messages.error(request,'not user found...!!!')
                return redirect('forgot')   
        
        user=User.objects.get(username=name) 
        token=str(uuid.uuid4())
        send_forget_password_mail(user, token )
        messages.success(request,'an email is send')
        return redirect('change') 

    except Exception as e:
        print(e)
    
    form = createuserform ()
    return render(request,'forgot-password.html',{'form':form})    







            
'''  
@allowed_user(allowed_roles=['admin'])    
def change(request , token):
    context={}
    try:
        user=profile.objects.get(forget_password_token=token)
        print(user)

    except Exception as e:
        print(e)
    
    form = createuserform ()
    return render(request,'changepassword.html',{'form':form})   
'''

def admin_login(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        user=User(email=email,password1=password1)
        if user is not None:
            form = login(request, user)
            #messages.success(request, ' welcome our brightwheel !!')
            return redirect('/admin')
        else:
            messages.info(request, 'account not exit plz register')

       
    form = createuserform ()
    return redirect('/admin')
   
   
    




    

# Create your views here.
