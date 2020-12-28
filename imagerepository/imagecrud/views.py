from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Image
from django.contrib.auth.models import User
from .models import UserImages

def index(request):
    template = loader.get_template('imagecrud/index.html')

    return HttpResponse(template.render({}, request))

def home(request):
    template = loader.get_template('templates/home.html')
    context = { "something" : 100 }

    return HttpResponse(template.render(context, request))

def create_user(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    print(username)
    user = User.objects.create_user(username,'', password)
    user.save()

    template = loader.get_template('imagecrud/mainpage.html')
    context = {
        'user' : user,
    }
    return HttpResponse(template.render(context, request))
# def index(request):
#     user = User()
#     user.save()
#     image = Image(name="art", price=10)
#     image.save()
#     # wallet_amount = user.wallet
#     # image_price = image.price
#     template = loader.get_template('imagecrud/index.html')
#     context = {
#         'user' : user,
#         'image' : image
#     }
#     return HttpResponse(template.render(context, request))

def buy(request, image_id, user_id):

    image = Image.objects.get(id=image_id)
    user = User.objects.get(id=user_id) 
    new_wallet = user.wallet - image.price
    user.wallet = new_wallet
    user.save()
    new_stock = Image.objects.get(id=image_id).stock - 1
    image.stock = new_stock
    image.save()
    owned_images = UserImages(image_id, user_id)
    owned_images.save()


    template = loader.get_template('imagecrud/buy.html')
    context = {
        'user' : user,
        'image' : image,
        'new_stock' : new_stock
    }
    return HttpResponse(template.render(context, request))
