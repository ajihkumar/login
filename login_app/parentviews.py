
from django.shortcuts import redirect, render

from login_app.forms import add_parentsform
from django.contrib import messages

from login_app.models import createparents, createparentss


def parent_page(request):
    return render(request,'main/parent.html')

def create_parent(request):
   
    if request.method == 'POST':
        form =add_parentsform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful." )
            return redirect("create_parent")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = add_parentsform()
    return render(request=request, template_name='project/create_parent.html', context={"form":form})
  

def list_parent(request):
    parent=createparentss.objects.all()
    count=createparentss.objects.all().count

    return render(request,'project/list_parent.html',{'parent':parent,'count':count})    