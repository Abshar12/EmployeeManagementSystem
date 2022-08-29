from django.shortcuts import render
from .models import *
from django.contrib.auth import logout , authenticate , login 
from django.shortcuts import render ,HttpResponseRedirect,redirect
from .forms import EmployeeAdd
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Create your views here.


def index(request):
    return render(request , 'index.html')



def admin_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request,email=email,password=password)
        print ( user is not None)
        if user is not None:
            login(request,user)
            
            return render(request,'welcome.html')

        
    else:
        return render(request,'admin_login.html')
    
    return render(request,'admin_login.html')




def admin_logout(request):
    logout(request)



def add_Employee(request):
    form = EmployeeAdd()
    if request.method=='POST':
        form = EmployeeAdd(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Employee added successfully")
            form=EmployeeAdd()
            
        else:
            form=EmployeeAdd()
            
    show=Employee.objects.all()

    return render(request,'add_employee.html',{'form':form,'stu':show})




def delete(request,id):
    if request.method == 'POST':
        pi = Employee.objects.get(pk=id)
        pi.delete()
        messages.success(request,"Employee deleted successfully")
        return redirect('addEmployee') 




def update(request,id):
    if request.method =='POST':
        pi = Employee.objects.get(pk=id)
        form = EmployeeAdd(request.POST , instance=pi)
        form.is_valid()
        form.save()
        messages.success(request,"Employee updated successfully")
    else:
        pi = Employee.objects.get(pk=id)
        form = EmployeeAdd(instance=pi) 
    return render(request,'edit_employees.html',{'form':form})

