from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'calorie'

urlpatterns = [
    path('', views.calorie_main, name='calorie'),
    path('get_calorie_info/', views.get_calorie_info, name='get_calorie_info')
]
