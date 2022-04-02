
from django.shortcuts import redirect, render


def staff(request):
    return render(request,'staff.html')