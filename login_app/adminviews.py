
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

from login_app.forms import add_studentform
from.models import datas

def superadmin_page(request):
    count = datas.objects.all().count()
    obj=datas.objects.all()
    
    return render(request,'project/superadmin_dashboard.html',{'count':count,'obj':obj})
def student_page(request):
   # user=User.objects.all()
    return render(request,'project/add_student.html')    

def admin_page(request):
    user=User.objects.all()
    obj=datas.objects.all()
    return render(request,'main/admin_page.html',{'user':user,'obj':obj})
def delete(request,id):
    user=User.objects.get(id=id)
    
    user.delete()
    
    return redirect('admin_page') 

def admin_site_register(request):
    
    if request.method == 'POST':
        form =add_studentform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request, "Registration successful." )
            return redirect("add_register")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = add_studentform()
    return render(request=request, template_name='project/add_student.html', context={"form":form})


    