from django.db import models

# Create your models here.
class media(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    price = models.CharField(max_length=200)
    description = models.CharField(max_length=200)




class useregister(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    username=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
