from django import forms
from .models import *
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class EmployeeAdd(forms.ModelForm):
    class Meta:
        model = Employee
        fields ='__all__'
    
   
       


class AdminAdd(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Admin
        # fields = ('email', 'date_of_birth','role')
        fields = ('first_name','last_name','email','password1','password2','role','is_admin')
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Admin
        # fields = ('first_name','last_name','email', 'password', 'date_of_birth', 'is_active', 'is_admin','is_deleted')
        fields = '__all__'
    def clean_password(self):
        return self.initial["password"]
