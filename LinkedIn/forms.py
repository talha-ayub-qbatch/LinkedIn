from dataclasses import field
from email import message
from tkinter import Widget
from django import forms
from .models import *

class UserForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)

class RegisterdForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['username','password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            # 'email': forms.EmailInput(attrs={'class':'form-control'}),
            # 'age': forms.TextInput(attrs={'class':'form-control'}),
        }
    