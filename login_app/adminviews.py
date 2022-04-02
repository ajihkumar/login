
from django.shortcuts import redirect, render
from django.contrib.auth.models import User


def admin_page(request):
    user=User.objects.all()
    return render(request,'admin_page.html',{'user':user})