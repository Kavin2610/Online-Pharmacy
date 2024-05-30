from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class HealthTip(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.URLField(max_length=200, blank=True, null=True)
    thumbnail = models.ImageField(blank=True, null=True)
    publication_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
# model for addtional details about the user
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=100, blank=True)
    phonenumber = models.CharField(max_length=20, blank=True)

class ContactUs(models.Model):
    name = models.TextField(max_length = 25)
    email = models.EmailField()
    subject = models.TextField(blank=True, null=True, max_length = 50)
    message = models.TextField(max_length = 500)

    def __str__(self):
        return self.name



