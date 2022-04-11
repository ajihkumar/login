from django.urls import path

from login_app import staffviews
from.import views
from .import staffviews,adminviews,parentviews

urlpatterns = [
    path('',views.home,name="home"),  
    path('register/',views.register,name="register"),
    path('signin/',views.signin,name="signin"),
    #path('signin/',auth_views.LoginView.as_view(template_name='signin.html'),name="signin"), 
    path('signup/',views.signup,name="signup"),
    path('forgot/',views.forgot,name="forgot"),
    #path('change/<token>/',views.change,name="change"),
    path('admin_login/',views.admin_login,name="adminlogin"),
    path('staff/',staffviews.staff,name="staff"),
    path('admin_page/',adminviews.admin_page,name="admin_page"),
    path('parents/',parentviews.parent_page,name="parents"),
    path('parent_list/',parentviews.list_parent,name="list_parent"),
    path('create_parent/',parentviews.create_parent,name="create_parent"),
    path('delete/<id>',adminviews.delete,name="delete"),
    path('superadmin/',adminviews.superadmin_page,name="superadmin"),
    path('add_register/',adminviews.admin_site_register,name="add_register"),


]    