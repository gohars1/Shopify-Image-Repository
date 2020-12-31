from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Image
from django.contrib.auth.models import User
from .models import UserImages

def index(request):
    template = loader.get_template('imagecrud/index.html')
    images = Image.objects.all()
    user = User.objects.get(username=request.user.username).userinfo
    context = { 'images' : images , 'user' : user }

    return HttpResponse(template.render(context, request))

def buy(request, image_id, user_id):

    image = Image.objects.get(id=image_id)
    user = User.objects.get(id=user_id).userinfo 
    new_wallet = user.wallet - image.price
    user.wallet = new_wallet
    user.save()
    new_stock = Image.objects.get(id=image_id).stock - 1
    image.stock = new_stock
    image.save()
    user = User.objects.get(username=request.user.username)
    if (UserImages.objects.filter(image_id=image,user_id=user).exists()):

        userimage = UserImages.objects.get(image_id=image,user_id=user)
        print(userimage.count)
        new_count = userimage.count + 1
        print(new_count)
        userimage.count = new_count
        print(userimage, userimage.count)
        userimage.save()
    else:

        owned_images = UserImages(image_id=image,user_id=user)
        owned_images.save()

    user = User.objects.get(username=request.user.username).userinfo
    template = loader.get_template('imagecrud/buy.html')
    images = Image.objects.all()

    context = { 'images' : images , 'user' : user }

    return HttpResponse(template.render(context, request))
