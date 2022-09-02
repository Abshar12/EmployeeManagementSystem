from urllib import response
from django.shortcuts import render
from .models import *
from django.contrib.auth import logout , authenticate , login 
from django.shortcuts import render ,HttpResponseRedirect,redirect,HttpResponse
from .forms import AdminAdd, EmployeeAdd
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
import csv


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


@login_required(login_url="/")
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
    return render(request,'add_employee.html',{'form':form})


def show_employee(request):   
    show=Employee.objects.all()
    p = Paginator(Employee.objects.all(),2)
    page = request.GET.get('page')
    Emp = p.get_page(page)
    return render(request,'show_emp.html',{'Emp':Emp})



def add_admin(request):
    form = AdminAdd()
    if request.method=='POST':
        form = AdminAdd(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Admin added successfully")
            form=AdminAdd()
        
        else:
            form=AdminAdd()
    return render(request,'add_admin.html',{'form':form})

def show_admin(request):
    show=Admin.objects.all()
    p = Paginator(Admin.objects.all(),2)
    page = request.GET.get('page')
    Adm = p.get_page(page)
    # return render(request,'add_employee.html',{'form':form,'stu':show})
    return render(request,'show_admin.html',{'Adm':Adm})




def delete_emp(request,id):
    if request.method == 'POST':
        pi = Employee.objects.get(pk=id)
        pi.delete()
        messages.success(request,"Employee deleted successfully")
        return redirect('showemp') 


def delete_adm(request,id):
    if request.method == 'POST':
        pi = Admin.objects.get(pk=id)
        pi.delete()
        messages.success(request,"Admin deleted successfully")
        return redirect('showadm')

    


def update_emp(request,id):
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


def update_adm(request,id):
    if request.method == 'POST':
        pi = Admin.objects.get(pk=id)
        form = AdminAdd(request.POST,instance=pi)
        form.is_valid()
        form.save()
    else:
        pi = Admin.objects.get(pk=id)
        form = AdminAdd(instance=pi)
    return render (request ,'edit_admin.html',{'form':form})


def show_emp_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename = Employees.csv'

    writer = csv.writer(response)
    show=Employee.objects.all()

    writer.writerow(['FirstName','LastName','Gender','Email','Address','Country','State','City','Pincode'])

    for emp in show:
        writer.writerow([emp.first_name,emp.last_name,emp.gender,emp.email,emp.address,emp.country,emp.state,emp.city,emp.pincode])
    
    return response


def show_adm_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename = Admin.csv'

    writer = csv.writer(response)
    show=Admin.objects.all()

    writer.writerow(['FirstName','LastName','Email','Role'])

    for adm in show:
        writer.writerow([adm.first_name,adm.last_name,adm.email,adm.role])
    
    return response