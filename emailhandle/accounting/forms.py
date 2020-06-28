from django.core.validators import MinLengthValidator, RegexValidator
from django_mongoengine.forms import *
from django import forms
class Accountform(forms.Form):
    NAME=forms.CharField(max_length=30)
    EMAIL=forms.EmailField(max_length=30)
    PASSWORD1=forms.CharField(max_length=30,validators=[MinLengthValidator(8)],help_text="Password Must Have Minimum 8 characters",widget=forms.PasswordInput())
    PASSWORD2=forms.CharField(max_length=30,widget=forms.PasswordInput())
