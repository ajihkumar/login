from email.mime import image
from multiprocessing import context
from tabnanny import check
from urllib import response

from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.shortcuts import redirect, render,HttpResponse
from login_app import models
from login_app.forms import add_staffform, createuserform, uploadform
from login_app.models import StudentExtra, createstaffs, upload_image
from django.contrib import messages
'''from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from login_app.serializers import postserializer

class uploadview(APIView):
    def get(self,request):
        return Response({'into':'helloword'})
 
class postview(ModelViewSet):
    queryset=upload_image.objects.all()
    serializer_class=postserializer
'''





def parent_page(request):
    return render(request,'main/parent.html')

def create_parent(request):
   
    if request.method == 'POST':
        form =createuserform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful." )
            return redirect("create_parent")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = createuserform()
    return render(request=request, template_name='project/create_parent.html', context={"form":form})
 
def list_activities(request):
    obj=StudentExtra.objects.all()
    return render(request,'view/list_activities.html',{'obj':obj}) 


def list_parent(request):
    #obj1=StudentExtra.objects.get(id=pk)
    obj=StudentExtra.objects.all()
    print(obj)
    img= uploadform()
    if request.method == "POST":
        form= uploadform()
        if form.is_valid():
            check=request.POST.getlist('boxes')
            print(check)
        
            for i in range(len(check)):
            #b=StudentExtra.objects.get(pk=i)
                b=models.upload_image()
           

                b.save()
                print(b)
        return redirect("upload_image")
        
    return render(request,'project/list_parent.html',{'obj':obj,'img':img}) 
def upload_images(request):
    #form=uploadform()
    #mydict={'form':form}
    #image=upload_image.objects.all()
    # obj = StudentExtra.objects.filter(id = request.POST.get('student'))
    # print(obj)
    # img= upload_image.objects.all()
    if request.method == 'POST':
        # form =uploadform(request.POST, request.FILES)
        student = StudentExtra.objects.get(id = request.POST.get('student'))
        img= upload_image.objects.filter(receiver = student)
        # if form.is_valid():
            #check=request.POST.getlist('boxes')
            #for i in range(len(check)):
                #check=upload_image()
                #check.id=pk
                #check.save()
            #form.sender = request.user
            #form.instance.student = request.student
            #form.receiver =request.user
            # form.save()
            
            # return redirect("upload_image")
        return render(request,'view/upload_image.html',{'img':img,'student':student})
           
    # else:
        # form=uploadform()
        
    # return render(request,'view/upload_image.html',{'img':img}) 


def delete_parent(request,id):
    parent=upload_image.objects.get(id=id)
    parent.delete()
    return redirect("upload_image")


def update_data_parent(request,id):
    parent=User.objects.get(id=id)
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        

        try:
            
            parent.first_name=first_name
            parent.last_name=last_name
            parent.username=username
            parent.email=email
            
            parent.address=address
            
            parent.save()
            return redirect("list_parent")

        except:
            messages.error(request, "Failed to Update Staff.")
            return redirect('updatedata_parent')

    return render(request,'update/parent_update.html',{'parent':parent})



'''def delete_parent(request,id):
    parent=User.objects.get(id=id)
    parent.delete()
    return redirect('staff_create')

'''
def parent_schedule(request):
    return render(request,'view\parent_schedule.html')

def post_image(request):
    try:
        if request.FILES.get('image'):
            student = StudentExtra.objects.get(id = request.POST.get('student'))
            upload_image.objects.create(sender = request.user,receiver=student,image = request.FILES.get('image'))
            return redirect('upload_image',id=student.id)
    except:
        return redirect('upload_image')