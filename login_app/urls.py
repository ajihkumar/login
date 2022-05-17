
from django.conf import settings
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView,LogoutView
from login_app import roomviews, staffviews
from.import views
from .import staffviews,adminviews,parentviews
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('',views.home,name="home"),  
    path('register/',views.register,name="register"),
    path('teachersignup/',views.teacher_signup_view,name='teachersignup'),  
        
    path('signin/',views.signin,name="signin"),
    path('afterlogin',views.afterlogin_view,name='afterlogin'),
    path('admin_signin/',auth_views.LoginView.as_view(template_name='admin_signin.html'),name="adminsignin"), 
    path('teacherlogin',LoginView.as_view(template_name='staff_login.html'),name='teacherlogin'),
    path('signup/',views.signup,name="signup"),
    path('forgot/',views.forgot,name="forgot"),
    #path('change/<token>/',views.change,name="change"),
    path('admin_login/',views.admin_login,name="adminlogin"),
    path('staff/',staffviews.staff,name="staff"),
    path('staff_create/',staffviews.staff_list,name="staff_create"),
    path('adminstaff_approve/',staffviews.admin_approve_teacher_view,name="adminstaff_approve"),
    path('staff_approve/<int:pk>',staffviews.approve_teacher_view,name="staff_approve"),
    path('staff_list/',staffviews.create_staff,name="staff_list"),
    path('admin_page/',adminviews.admin_page,name="admin_page"),
    path('parents/',parentviews.parent_page,name="parents"),
    path('parent_list/',parentviews.list_parent,name="list_parent"),
    path('create_parent/',parentviews.create_parent,name="create_parent"),
    path('superadmin/',adminviews.superadmin_page,name="superadmin"),
    #path('enrolment/',adminviews.enroolment,name="enroolment"),
    path('add_register/',adminviews.admin_site_register,name="add_register"),

#update delete
    #path('delete/<id>',adminviews.delete,name="delete"),
    path('delete/<id>',staffviews.delete_staff,name="delete_staff"),
    path('delete_student/<int:pk>',adminviews.delete_student_view,name="delete_student"),
    path('delete_parent/<id>',parentviews.delete_parent,name="delete_parent"),
    path('updatedata/<int:pk>',staffviews.update_data,name="updatedata"),
    path('updatedata_parent/<int:id>',parentviews.update_data_parent,name="updatedata_parent"),
    path('update_student/<int:pk>',adminviews.update_student_view,name="update_student"),

#views
    path('student_views/<int:pk>',adminviews.student_views,name="student_views"),
    path('upload_image/',parentviews.upload_images,name="upload_image"),
    #path('search/<int:id>',adminviews.student_serach,name="search"),
    path('list_activities/',parentviews.list_activities,name="listactivities"),

#rooms
    path('rooms/',roomviews.rooms,name="rooms"),
    
]    
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)