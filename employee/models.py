from django.contrib.auth.models import AbstractBaseUser ,BaseUserManager , UserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin




# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class City(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Gender(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Employee(models.Model):
    first_name = models.CharField (max_length=50)
    last_name = models.CharField (max_length=50)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE , null=True)
    email = models.CharField (max_length=50, unique=True)
    password = models.CharField (max_length=800)
    address = models.CharField (max_length=50)
    country = models.ForeignKey(Country ,on_delete=models.SET_NULL , null=True)
    state = models.ForeignKey(State ,on_delete=models.SET_NULL , null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL , null=True)
    pincode = models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,blank=True,null=True)
    is_deleted = models.BooleanField(default=0)

    def __str__(self):
        return self.first_name 
    
    

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
         
class MyUserManager(BaseUserManager):
    def create_user(self,role, email, date_of_birth, password=None):
        
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            role=role
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,role, email,date_of_birth,password=None,):
       
        user = self.create_user(email,password=password,date_of_birth=date_of_birth,role=role)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Admin(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField( max_length=50)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
    # date_of_birth = models.DateField()
    created_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,blank=True,null=True)
    role = models.ForeignKey(Role,on_delete=models.DO_NOTHING,default=None,null=True)
    is_deleted =  models.BooleanField(default=0)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
       return True

    @property
    def is_staff(self):
       return self.is_admin




class Profile(models.Model):
    first_name = models.OneToOneField(Admin , on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username




    
    
