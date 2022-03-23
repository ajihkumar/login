from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
class LoginForm(AuthenticationForm):
    def __init__(self, *args,  **kwargs): 
       super().__init__(*args, **kwargs)
       self.fields["username"].widget.attrs.update({
          'name':'username',
          'type':'text',
          'class':'form-control',
          'autocomplete':'off',
          'placeholder':'Full Name',
          'aria-label':'Full Name',

       })
       self.fields["password"].widget.attrs.update({
          'name':'password',
          'type':'password',
          'class':'form-control',
          'autocomplete':'off',
          'placeholder':'password',
          'aria-label':'password',

       })
    class Meta:
       model=User
       fields=['username','password1']


      



class createuserform(UserCreationForm):
  
   def __init__(self, *args,  **kwargs): 
       super().__init__(*args, **kwargs)
       self.fields["username"].widget.attrs.update({ 
          'name':'username',
          'type':'text',
          'class':'form-control',
          'autocomplete':'off',
          'placeholder':'Full Name',
          'aria-label':'Full Name',
       })
       self.fields["email"].widget.attrs.update({
          'name':'email',
          'type':'email',
          'class':'form-control',
          'autocomplete':'off',
          'placeholder':'Email Address',
          'aria-label':'Email Address',

       })
       self.fields["password1"].widget.attrs.update({
          'name':'password1',
          'type':'password',
          'class':'form-control',
          'autocomplete':'off',
          'placeholder':'password',
          'aria-label':'password',

       })
       self.fields["password2"].widget.attrs.update({
          'name':'password2',
          'type':'password',
          'class':'form-control',
          'autocomplete':'off',
          'placeholder':'confirm password',
          'aria-label':'password',

       })



   class Meta:
      model=User
      fields=['username','email','password1','password2']

   

      

          