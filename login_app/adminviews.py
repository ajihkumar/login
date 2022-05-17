

from django.contrib.auth.decorators import login_required, user_passes_test
from login_app import models
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from login_app import forms

from login_app.forms import add_studentform
from.models import StudentExtra, datas


def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()


def is_teacher(user):
    return user.groups.filter(name='TEACHER').exists()


def afterlogin_view(request):
    if is_admin(request.user):
        return render("signup")

# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)


def superadmin_page(request):
    todal_child = StudentExtra.objects.all().count()
    active = StudentExtra.objects.all().filter(status="active").count()
    waitlist = StudentExtra.objects.all().filter(status="waitlist").count()
    toured = StudentExtra.objects.all().filter(status="toured").count()
    applied = StudentExtra.objects.all().filter(status="applied").count()
    prospects = StudentExtra.objects.all().filter(status="prospects").count()
    obj = StudentExtra.objects.all()
    mydict = {
        'active': active,
        'toured': toured,
        'waitlist': waitlist,
        'applied': applied,
        'todal_child': todal_child,
        'prospects': prospects,
        'obj': obj

    }

    return render(request, 'project/superadmin_dashboard.html', context=mydict)


def student_page(request):
   # user=User.objects.all()
    return render(request, 'project/add_student.html')


def admin_page(request):
    user = User.objects.all()
    obj = datas.objects.all()
    return render(request, 'main/admin_page.html', {'user': user, 'obj': obj})


def delete(request, id):
    user = User.objects.get(id=id)

    user.delete()

    return redirect('admin_page')


def admin_site_register(request):

    form1 = forms.StudentUserForm()
    form2 = forms.StudentExtraForm()
    mydict = {'form1': form1, 'form2': form2}
    if request.method == 'POST':
        form1 = forms.StudentUserForm(request.POST)
        form2 = forms.StudentExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            print("form is valid")
            user = form1.save()
            user.set_password(user.password)
            user.save()

            f2 = form2.save(commit=False)
            f2.user = user
            f2.status
            f2.save()

            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
            messages.success(request, "Registration successful.")
            return redirect("add_register")
        else:
            print("form is invalid")
        return redirect('add_register')

    return render(request=request, template_name='project/add_student.html', context=mydict)


def update_student_view(request, pk):
    student = models.StudentExtra.objects.get(id=pk)
    user = models.User.objects.get(id=student.user_id)
    form1 = forms.StudentUserForm(instance=user)
    form2 = forms.StudentExtraForm(instance=student)
    mydict = {'form1': form1, 'form2': form2}
    if request.method == 'POST':
        form1 = forms.StudentUserForm(request.POST, instance=user)
        form2 = forms.StudentExtraForm(request.POST, instance=student)
        print(form1)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()
            f2 = form2.save(commit=False)
            f2.status
            f2.save()
            return redirect("superadmin")
    return render(request, 'update/student_update.html', mydict)


def student_views(request, pk):
    obj = StudentExtra.objects.get(id=pk)
    user = User.objects.get(id=obj.user_id)
    return render(request, 'view/studentviews.html', {'obj': obj, 'user': user})


def delete_student_view(request, pk):
    student = models.StudentExtra.objects.get(id=pk)
    user = models.User.objects.get(id=student.user_id)
    user.delete()
    student.delete()
    return redirect('superadmin')
