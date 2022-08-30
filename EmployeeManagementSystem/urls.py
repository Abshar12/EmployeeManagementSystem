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
    path('delete/<int:id>', delete, name='delete'),
    path('<int:id>',update,name='update'),
    path('addAdmin',add_admin,name='addAdmin'),
    path('resetPassword',auth_views.PasswordResetView.as_view(),name='reset_password'),
    path('resetPassword_sent',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/token/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('resetPasswordComlete',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),


]
