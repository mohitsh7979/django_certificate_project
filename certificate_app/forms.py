from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

from .models import Enrollment



class Create_Account_Form(UserCreationForm):

    class Meta:

        model = User
        fields = ['username','email']


class login_form(AuthenticationForm):
    username = forms.CharField(
        label='username', widget=forms.TextInput(attrs={'placeholder': 'Username','class':'form-control'}))
    
    password = forms.CharField(
        label='password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password','class':'form-control'}))

    
  



class certificate_form(forms.ModelForm):

    class Meta:

        model = Enrollment
        fields = ['certification','enrollment_date','completion_date']
        widgets = {

            'certification':forms.Select(attrs={'class':'form-control'}),
            'enrollment_date':forms.DateInput(attrs={'class':'form-control picker'}),
            'completion_date':forms.DateInput(attrs={'class':'form-control picker'})
        
        }