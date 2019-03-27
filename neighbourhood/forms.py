from django import forms
from .models import *

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('name', 'image', 'description', 'cartegory', 'profile', 'phone_number')
