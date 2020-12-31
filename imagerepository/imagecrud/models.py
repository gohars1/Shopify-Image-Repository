from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Image(models.Model):
    imgurl = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=10)

# class User(models.Model):
#     wallet = models.IntegerField(default=200)
#     # owned_images = models.ForeignKey(Image, on_delete=models.CASCADE, blank = True, null = True)
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet = models.IntegerField(default=200)

class UserImages(models.Model):
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE, blank = True, null = True) 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True)

@receiver(post_save, sender=User)
def create_user_info(sender, instance, created, **kwargs):
    if created:
        UserInfo.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_info(sender, instance, **kwargs):
    instance.userinfo.save()