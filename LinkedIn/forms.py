from email import message
from django import forms
from .models import *

class UserForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)