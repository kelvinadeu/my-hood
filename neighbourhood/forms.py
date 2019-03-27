from django import forms
from .models import *

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('name', 'image', 'description', 'cartegory', 'phone_number')
