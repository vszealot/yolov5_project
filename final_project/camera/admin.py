# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.
from .models import Image, FoodInfo, MealInfo

admin.site.register(Image)
admin.site.register(FoodInfo)
admin.site.register(MealInfo)
