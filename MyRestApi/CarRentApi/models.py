from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

# Create your models here.
class UserProfileManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User must have email!")

        email = self.normalize_email(email)
        user = self.model(email=email)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_owner(self,email,password):
        user=self.create_user(email,password)
        user.is_owner=True
        user.save(using=self._db)

        return user

    def create_customer(self,email,password):
        user=self.create_user(email,password)
        user.is_customer=True
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_owner=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=False)
    objects = UserProfileManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email
class Test(models.Model):
    test=models.BooleanField(default=False)

class Customer(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True,related_name='customer')


    def __str__(self):
    	return self.user.email


class Owner(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True,related_name='owner')


    def __str__(self):
    	return self.user.email

# username:this.state.name,
#             phone:this.state.phone,
#             roomname:this.props.item.roomName,
#             roomtype:this.props.item.roomType,
#             roomno:this.props.item.roomNo,
#             date:this.props.item.date,
#             price:this.props.item.price,
#             total:this.props.item.total,
#             bookTime:dateFormat(new Date(), "ddd mmm d yyyy, h:MM:ss TT"),
#             userid:this.props.userId

class Book(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='book_user')
    username=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200)
    roomname=models.CharField(max_length=200)
    roomtype=models.CharField(max_length=200)
    roomno=models.CharField(max_length=20,blank=False)
    date=models.CharField(max_length=100, blank=False)
    price = models.CharField(max_length=20, blank=False)
    bookTime=models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.user.email