from django import forms
from .models import *

class Search1(forms.Form):
    search = forms.CharField(label='Search') #2

class Update(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'