
from django.conf import settings
from django.core.mail import send_mail

def send_forget_password_mail(email, token):
   
    subject='your forgot password link'
    message= f'HI,click on the link to reset your password http://127.0.0.1:8000/change/{token}/'
    email_from='ajitharunachalam9100@gmail.com'
    recipient_list=[email]
    send_mail(subject,message,email_from,recipient_list,fail_silently=True)
 
