from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return f' Message From  {self.name}'

cats = [("......","......"),("Bikes","Bikes",),("Cars","Cars"),("Heavy-Motors","Heavy-Motors")]
class Products(models.Model):
    sno=models.AutoField(primary_key=True)
    category=models.CharField(max_length=100,choices=cats,default="")
    timeslap=models.TimeField(blank=True)
    author=models.CharField(max_length=100)
    Image= models.ImageField(upload_to='mysite/images', default="")

    def __str__(self):
        return f" post by {self.author} of {self.category}"

class Dealership(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    registeration_number=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    number=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return f' Applied From  {self.name}'
class glay_gallery(models.Model):
    image=models.ImageField(null=True,blank=True,upload_to="mysite/images")
    picture_title=models.CharField(max_length=100, blank=True)
    
    # def __str__(self):
    #     return f"{self.image} {self.picture_title}
    