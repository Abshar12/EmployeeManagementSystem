from cProfile import label
from django import forms
from .models import *
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class EmployeeAdd(forms.ModelForm):
    class Meta:
        model = Employee
        fields =('first_name','last_name','gender','email','address','country','state','city','pincode','created_at')
        widgets={
            'first_name': forms.TextInput(attrs={'class':'form-control col-md-6'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control col-md-6'}),
            'address' : forms.TextInput(attrs={'class':'form-control col-md-6'}),
            'email' : forms.EmailInput(attrs={'class':'form-control col-md-6'}),
            'gender':forms.Select(attrs={'class':'form-control col-md-6'}),
            'country':forms.Select(attrs={'class':'form-control col-md-6'}),
            'state':forms.Select(attrs={'class':'form-control col-md-6'}),
            'city':forms.Select(attrs={'class':'form-control col-md-6'}),
            'pincode':forms.NumberInput(attrs={'class':'form-control col-md-6'}),

            
        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['state'].queryset = State.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['state'].queryset=State.objects.filter(country_id=country_id).order_by('name')
            except (ValueError,TypeError):
                pass
        elif self.instance.pk:
            self.fields['state'].queryset = self.instance.country.state_set.order_by('name')
   
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset=City.objects.filter(state_id=state_id).order_by('name')
            except (ValueError,TypeError):
                pass
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.state.city_set.order_by('name')
       




class AdminAdd(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control col-md-6'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class':'form-control col-md-6'}))

    class Meta:
        model = Admin
        
        fields = ('first_name','last_name','email','role','password1','password2')
        widgets={
            'first_name': forms.TextInput(attrs={'class':'form-control col-md-6','id':'firstname'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control col-md-6','id':'lastname'}),
            'email' : forms.EmailInput(attrs={'class':'form-control col-md-6','id':'email'}),
            'role' : forms.Select(attrs={'class':'form-control col-md-6'})
            
            
        }
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
