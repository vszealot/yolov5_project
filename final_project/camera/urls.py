from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'camera_main'

urlpatterns = [
    path('', views.camera, name='camera'),
    path('get_img/', views.get_img, name='get_img'),
    path('put_meal_info/', views.put_meal_info, name='put_meal_info'),
    # url(r'^stream2/$', views.stream2, name='stream2'),
]
