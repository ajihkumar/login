
from django.shortcuts import redirect, render


def parent_page(request):
    return render(request,'parent.html')