from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user_details(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    choice_field = (
        ('Doctor','Doctor'),('Patient','Patient')
    )
    User_Type = models.CharField(max_length=20,choices=choice_field)
    image = models.ImageField(upload_to='media/')
    address = models.TextField(max_length=150)
    def __str__(self):
        return self.User_Type

class Category(models.Model):
    cty = models.CharField(max_length=30)
    def __str__(self):
        return self.cty

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image  = models.ImageField(upload_to='post/',blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    summary = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    Publish = models.BooleanField(default=False)