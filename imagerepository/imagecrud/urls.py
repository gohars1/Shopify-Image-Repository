from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('buy/', views.buy, name='buy'),
    path('<int:image_id>/<int:user_id>/buy/', views.buy, name='buy'),
]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)