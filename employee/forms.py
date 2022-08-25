from django import forms
from .models import *

class EmployeeAdd(forms.ModelForm):
    class Meta:
        model = Employee
        fields ='__all__'
       
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['state'].queryset = State.objects.none()

