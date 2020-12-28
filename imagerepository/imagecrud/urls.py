from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('buy/', views.buy, name='buy'),
    path('<int:image_id>/<int:user_id>/buy/', views.buy, name='buy'),
]