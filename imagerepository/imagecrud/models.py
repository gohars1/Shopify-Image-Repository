from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=10)

# class User(models.Model):
#     wallet = models.IntegerField(default=200)
#     # owned_images = models.ForeignKey(Image, on_delete=models.CASCADE, blank = True, null = True)
# class UserInfo(models.Model):
#     wallet = models.
class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet = models.IntegerField(default=200)

class UserImages(models.Model):
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE, blank = True, null = True) 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True)   