
from multiprocessing import context
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from django.shortcuts import redirect, render,HttpResponse
from django.urls import reverse
from login_app import models
from django.contrib.auth import get_user_model
from login_app.forms import TeacherExtraForm, add_staffform, createuserform, createuserform1, createuserform2
from login_app.models import CustomUser, TeacherExtra, createstaffs
from django.contrib import messages


def staff(request):
    return render(request,'main/staff.html')

def staff_list(request):
    User = get_user_model()
    staff1 = User.objects.all()
    staff=TeacherExtra.objects.all().filter(status=True)
    staff1=TeacherExtra.objects.all().filter(status=True).count()
    return render(request,'project/staff_create.html',{'staff':staff,'staff1':staff1})

def admin_approve_teacher_view(request):
    User = get_user_model()
    staff1 = User.objects.all()
    teachers=models.TeacherExtra.objects.all().filter(status=False)
    return render(request,'project/staff_approve.html',{'teachers':teachers,'staff1':staff1})    
def approve_teacher_view(request,pk):
    teacher=models.TeacherExtra.objects.get(id=pk)
    teacher.status=True
    teacher.save()
    return redirect('adminstaff_approve')


def create_staff(request):
    form =createuserform()
    form1 =TeacherExtraForm()
    mydict={'form':form,'form1':form1}
    if request.method == 'POST':
        form =createuserform(request.POST, request.FILES)
        form1 =TeacherExtraForm(request.POST, request.FILES)
        if form.is_valid() and form1.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()

            f2=form1.save(commit=False)
            f2.user=user
            f2.status=True
            f2.save()

            my_teacher_group = Group.objects.get_or_create(name='STAFF')
            my_teacher_group[0].user_set.add(user)

            messages.success(request, "Registration successful." )
            return redirect("staff_list")
        messages.error(request, "Unsuccessful registration. Invalid information.")
     
    return render(request=request, template_name='project/list_staff.html', context=mydict)
      
def update_data(request,pk):
    staff=models.TeacherExtra.objects.get(id=pk)
    user=models.User.objects.get(id=staff.user_id)
    form1=createuserform(instance=user)
    form2=TeacherExtraForm(instance=staff)
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=createuserform(request.POST,instance=user)
        form2=TeacherExtraForm(request.POST,instance=staff)
        print(form1)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.status=True
            f2.save()
            
            return redirect('staff_create')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    
    
    return render(request,'update/staff_update.html',context=mydict)


'''    if request.method =='POST':

       first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        #date_joined =request.POST['date_joined']
        address = request.POST['address']
        #status  = request.POST['status']
        
        try:
            staff=CustomUser.objects.get(id=id)
            staff.first_name=first_name
            staff.last_name=last_name
            staff.username=username
            staff.email=email
            #staff.date_joined= date_joined
            staff.address=address
            #staff.status =status 
            
            
            
            staff.save()
            return redirect("staff_create")

        except:
            messages.error(request, "Failed to Update Staff.")
            return redirect('updatedata')



          
    

    return render(request,'update/staff_update.html', {'staff':staff })

'''

def delete_staff(request,id):
    staff=CustomUser.objects.get(id=id)
    staff.delete()
    return redirect('staff_create')
