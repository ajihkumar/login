"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from login import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('login_app.urls')),



#reset password
 #path('password_reset/',auth_views.PasswordResetView.as_view(template_name='forgot-password.html'),name="forgot"),
 #path('password_reset/confirm/',auth_views.PasswordResetConfirmView.as_view(),name="confirm"),
 #path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name="done"),    
 #path('password_reset/complete/',auth_views.PasswordResetCompleteView.as_view(),name="signin"),

]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


