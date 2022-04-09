
from django.shortcuts import redirect, render


def parent_page(request):
    return render(request,'main/parent.html')

def parent_edit(request):
    return render(request,'project/parent_edit.html')    