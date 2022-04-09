
from django.shortcuts import redirect, render


def staff(request):
    return render(request,'main/staff.html')