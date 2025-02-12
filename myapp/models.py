from django.db import models
from django.contrib.auth.models import User 

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


















class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(media, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return float(self.product.price) * self.quantity

    def __str__(self):
        return f"{self.user.username}'s cart"