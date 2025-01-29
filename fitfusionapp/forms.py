from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import bench
from .models import contactdetail
from .models import billinginfo
from captcha.fields import CaptchaField


class signform(forms.Form):
    email=forms.EmailField(max_length=200, required=True)
    password=forms.CharField(widget=forms.PasswordInput, required=True)

class registerform(forms.Form):
    first_name=forms.CharField(max_length=200, required=True)
    last_name=forms.CharField(max_length=200, required=True)
    email=forms.EmailField(max_length=200, required=True)
    passwd=forms.CharField(widget=forms.PasswordInput, required=True)
    phone_number=forms.IntegerField()
    captcha = CaptchaField() 



class contactform(forms.ModelForm):
    class Meta:
        model=contactdetail
        fields=['name','email','website','comment']


class billingform(forms.ModelForm):
    class Meta:
        model = billinginfo
        fields = ['deliver', 'user', 'phone']