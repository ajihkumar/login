


from dataclasses import Field
from multiprocessing import Value
from optparse import Option
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django import forms
from .models import CustomUser, createparentss, createstaffs, datas, upload_image
from login_app import models


class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
      



class createuserform(forms.ModelForm):
  class Meta:
      model=User
      fields=(
      'first_name','last_name',
      'username','email',
      'address','password',
      )
class TeacherExtraForm(forms.ModelForm):
    class Meta:
        model=models.TeacherExtra
        fields=['mobile','status']      
class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','address','email']
class StudentExtraForm(forms.ModelForm):
    class Meta:
        model=models.StudentExtra
        fields=['mobile','status','Dob','Age','Gender','parentname'] 

class uploadform(forms.ModelForm):
    class Meta:
         model=upload_image
         fields=['image',]




class createuserform1(UserCreationForm):
   class Meta(UserCreationForm.Meta):
      model=CustomUser
      fields=(
      'first_name','last_name',
      'username','email',
      'address',
      )

class createuserform2(forms.ModelForm):
   class Meta:
      model=CustomUser
      fields=('first_name','last_name',
      'username','email',
      'status','address',
      )



class DateInput(forms.DateInput):
    input_type = 'date'
    
class add_studentform(forms.ModelForm):
    def __init__(self, *args,  **kwargs): 
       super().__init__(*args, **kwargs)
       self.fields["Firstname"].widget.attrs.update({ 
          'name':'Firstname',
          'type':'text',
          'class':'form-control',
          'autocomplete':'on',
          'placeholder':'First Name',
          'aria-label':'First Name',
       })
       self.fields["Secondname"].widget.attrs.update({ 
          'name':'Secondname',
          'type':'text',
          'class':'form-control',
          'autocomplete':'on',
          'placeholder':'Second Name',
          'aria-label':'Second Name',
       })
       self.fields["mail"].widget.attrs.update({ 
          'name':'mail',
          'type':'email',
          'class':'form-control',
          'autocomplete':'on',
          'placeholder':'mail',
          'aria-label':'mail',
       })
       self.fields["Dob"].widget.attrs.update({ 
          
       })
       self.fields["Age"].widget.attrs.update({ 
          'name':'Age',
          'type':'text',
          'class':'form-control',
          'autocomplete':'on',
          'placeholder':'Enter Your Age',
          'aria-label':'Enter Your Age',
       })
       self.fields["Gender"].widget.attrs.update({ 
          'name':'Gender',
          
       })
       self.fields["Address"].widget.attrs.update({ 
          'name':'Address',
          'type':'text',
          'class':'form-control',
          'autocomplete':'on',
          'placeholder':'Address',
          'aria-label':'Address',
       })
    class Meta():
      model = datas
      fields = '__all__'
      widgets = {
            'Dob': DateInput() 
            
         
            
        }
   
#create parents

class add_parentsform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password', }))
    def __init__(self, *args,  **kwargs): 
       super().__init__(*args, **kwargs)
       self.fields["firstname"].widget.attrs.update({ 
          'name':'firstname',
          'type':'text',
          'class':'form-control',
          'autocomplete':'on',
          'placeholder':'First Name',
          'aria-label':'First Name',
       })
       self.fields["secondname"].widget.attrs.update({ 
          'name':'secondname',
          'type':'text',
          'class':'form-control',
          'autocomplete':'on',
          'placeholder':'Second Name',
          'aria-label':'Second Name',
       })
       self.fields["username"].widget.attrs.update({ 
          'name':'username',
          'type':'text',
          'class':'form-control',
          'autocomplete':'on',
          'placeholder':'User Name',
          'aria-label':'User Name',
       })
       self.fields["mail"].widget.attrs.update({ 
          'name':'mail',
          'type':'email',
          'class':'form-control',
          'autocomplete':'on',
          'placeholder':'mail',
          'aria-label':'mail',
       }) 
       self.fields["address"].widget.attrs.update({ 
          'name':'address',
          'type':'text',
          'class':'form-control',
          'autocomplete':'on',
          'placeholder':'Address',
          'aria-label':'Address',
       })
       self.fields["zip_code"].widget.attrs.update({ 
          'name':'zip_code',
          'type':'text',
          'class':'form-control',
          'autocomplete':'on',
          'placeholder':'zip_code',
          'aria-label':'zip_code',
       })
    class Meta():
      model = createparentss
      fields = '__all__'
      
#create staffs 

class add_staffform(forms.ModelForm):
    password = forms.CharField(widget=forms.TextInput(attrs={'name':'password','class':'form-control','type':'password','placeholder':'Password','autocomplete':'off'}))
    
    
    
    class Meta():
      model = CustomUser
      fields = '__all__'
           
    