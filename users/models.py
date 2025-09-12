from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager
from cloudinary.models import CloudinaryField
# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('student','Student'),
        ('teacher','Teacher'),
        ('admin','Admin')
    )
    username = None
    profile_picture = CloudinaryField('image', blank=True, null=True)
    # profile_picture = models.ImageField(
    #     upload_to='profile_pictures/',  
    #     blank=True,
    #     null=True,
        
    # )
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True,null=True)
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    role = models.CharField(max_length=10,choices=ROLE_CHOICES,default='student')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.get_full_name()}"