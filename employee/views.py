from logging import lastResort
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


@login_required(login_url='adminLogin')
def addEmployee(request):
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


def add_Employee(request):
    country = Country.objects.all()
    d={'country':country}
    gender = Gender.objects.all()
    g ={'gender':gender}
    
    if request.method=='POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        address = request.POST['address']
        country = request.POST['country']
        state = request.POST['state']
        city = request.POST['city']
        pincode = request.POST['pincode']
        gender = request.POST['gender']
        created_at = request.POST['createdat']
        employees = Employee(first_name=first_name,last_name=last_name,gender=gender,email=email,address=address,country_id=country,state_id=state,city_id=city,pincode=pincode,created_at=created_at)
        employees.save()
        messages.success(request,"Employee added successfully")
        

    return render(request,'add_employee.html',d)


# def add_Employee(request):
    
#     if request.method=='POST':
        
#         if form.is_valid():
#             form.save()
#             messages.success(request,"Employee added successfully")
            
        
#         else:
#             pass
#     return render(request,'add_employee.html')


def show_employee(request):   
    show=Employee.objects.all()
    p = Paginator(Employee.objects.all(),2)
    page = request.GET.get('page')
    Emp = p.get_page(page)
    return render(request,'show_emp.html',{'Emp':Emp})



# def add_admin(request):
#     form = AdminAdd()
#     if request.method=='POST':
#         form = AdminAdd(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,"Admin added successfully")
#             form=AdminAdd()
        
#         else:
#             form=AdminAdd()
#     return render(request,'add_admin.html',{'form':form})

def add_admin(request):
    role = Role.objects.all()
    if request.method=='POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['password']
        created_at = request.POST['createdat']
        admin = Admin(first_name=first_name,last_name=last_name,email=email,password=password,role_id=role,created_at=created_at)
        admin.save()
        messages.success(request,"Admin added successfully")
    return render(request,'add_admintest.html',{'role':role})



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

    


# def update_emp(request,id):
#     country = Country.objects.all()
    
#     if request.method =='POST':
#         pi = Employee.objects.get(pk=id)
#         form = EmployeeAdd(request.POST , instance=pi)
#         if form.is_valid():
#             form.save()
#             messages.success(request,"Employee updated successfully")
#     else:
#         pi = Employee.objects.get(pk=id)
#         form = EmployeeAdd(instance=pi) 
#         messages.success(request,"cannot update now")
#     return render(request,'edit_employees1.html',{'country':country,'form':form,'edit':pi})




def update_emp(request,id):
    country = Country.objects.all()
    
    emp = Employee.objects.get(id=id)
   
    return render(request,'edit_employees1.html',{'edit':emp,'country':country})

def updated_emp(request,id):
    emp = Employee.objects.get(id=id)
    form = EmployeeAdd(request.POST,instance=emp)
    if form.is_valid():
        form.save()
        messages.success(request,"Employee updated successfully")
    return render (request,'edit_employees1.html',{'edit':emp})

    


def update_adm(request,id):
    if request.method == 'POST':
        pi = Admin.objects.get(pk=id)
        form = AdminAdd(request.POST,instance=pi)
        form.is_valid()
        form.save()
        messages.success(request,"Admin updtaed successfully")
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
 
# def country(request):
#     country = Country.objects,all()
#     d={'country':country}
#     return render(request,'add_employee2.html',d)

def load_states(request):
    country_id=request.GET.get('country_id')
    states = State.objects.filter(country_id=country_id)
    return render(request,'states.html',{'states':states})


def load_cities(request):
    state_id=request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id)
    return render(request,'cities.html',{'cities':cities})




# import uuid
# from django.core.mail import send_mail
# def ForgetPassword(request):
#     try:
#         if request.method == 'POST':
#             first_name = request.POST.get('first_name')
            
#             if not Admin.objects.filter(first_name=first_name).first():
#                 messages.success(request, 'Not user found with this username.')
#                 return redirect('/forget-password/')
            
#             user_obj = Admin.objects.get(first_name=first_name)
#             token = str(uuid.uuid4())
#             profile_obj= Profile.objects.get(user = user_obj)
#             profile_obj.forget_password_token = token
#             profile_obj.save()
#             send_mail(user_obj.email , token)
#             messages.success(request, 'An email is sent.')
#             return redirect('/forget-password/')
                
    
    
#     except Exception as e:
#         print(e)
#     return render(request , 'forget-password.html')