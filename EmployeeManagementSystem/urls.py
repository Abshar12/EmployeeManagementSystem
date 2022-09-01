"""EmpMngSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from itertools import pairwise
from unicodedata import name
from django.contrib import admin
from django.urls import path
from employee.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index , name='index'),
    path('' ,admin_login , name = 'adminLogin'),
    path('adminLogout', admin_logout , name='adminLogout'),
    path('addemployee',add_Employee,name='addEmployee'),
    path('delete/<int:id>', delete_emp, name='delete'),
    path('updateemp/<int:id>',update_emp,name='update'),
    path('addAdmin',add_admin,name='addAdmin'),
    path('showemp',show_employee,name='showemp'),
    path('showadm',show_admin,name='showadm'),
    path('updateadm/<int:id>',update_adm,name='updateadm'),
    path('deleteadm/<int:id>',delete_adm,name='deleteadm')



]
