from django.shortcuts import redirect, render



def rooms(request):
    return render(request,'project/rooms.html')
