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
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index , name='index'),
    path('login/' ,admin_login , name = 'adminLogin'),
    path('adminLogout/', admin_logout , name='adminLogout'),
    path('login/addemployee/',add_employee,name='addEmployee'),
    path('delete/<int:id>/', delete_emp, name='delete'),
    path('updateemp/<int:id>/',update_emp,name='update'),
    path('login/addadmin/',add_admin,name='addAdmin'),
    path('showemp/',show_employee,name='showemp'),
    path('showadm/',show_admin,name='showadm'),
    path('updateadm/<int:id>/',update_adm,name='updateadm'),
    path('deleteadm/<int:id>/',delete_adm,name='deleteadm'),
    path('emp_csv/',show_emp_csv,name='emp_csv'),
    path('adm_csv/',show_adm_csv,name='adm_csv'),
    path('ajax/load-states/',load_states,name='ajax_load_states'),
    path('ajax/load-cities/',load_cities,name='ajax_load_cities'),
    # path('change-password/<token>',change_password,name='change_password'),
    # path('forget-password/',forget_password,name='forget-password'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)







