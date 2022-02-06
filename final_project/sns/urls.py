from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'sns'

urlpatterns = [
    path('', views.sns_main, name='sns'),
    path('calorie_page', views.calorie_main, name='calorie')
]