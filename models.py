from django.db import models
from django.utils import timezone

# Create your models here.
class Your_Post(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    integer= models.IntegerField()
    is_enable = models.BooleanField(default=True)
    publish_data = models.DateField(auto_now_add=True)
    created_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/",blank=True,null=True)
    image_2 = models.ImageField(upload_to="images/",blank=True,null=True)
    image_3 = models.ImageField(upload_to="images/",blank=True,null=True)
    image_4 = models.ImageField(upload_to="images/",blank=True,null=True)
    slug_field = models.SlugField()

class Photo(models.Model):
    image = models.ImageField(upload_to="images/")
   # image_2 = models.ImageField(upload_to="images/",blank=True,null=True)
  #  image_3 = models.ImageField(upload_to="images/",blank=True,null=True)
   # image_4 = models.ImageField(upload_to="images/",blank=True,null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
class CustomUser(models.Model):
    pass
class User_serach_Form(models.Model):
    query = models.CharField(max_length=100)  
