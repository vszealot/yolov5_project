# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name


class FoodInfo(models.Model):
    food_id = models.AutoField(primary_key=True)
    food_name = models.CharField(unique=True, max_length=200)
    calorie = models.IntegerField(default=0)

    # def __str__(self):
    #     return self.food_id


class MealInfo(models.Model):
    username = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="mealinfo", db_column="username", to_field="username")
    food_name = models.ForeignKey(FoodInfo, on_delete=models.CASCADE, related_name="mealinfo", db_column="food_name", to_field="food_name")
    # input_object_id = models.CharField(max_length=200)
    output_object_id = models.CharField(max_length=200)
    pub_time = models.CharField(max_length=10)
    pub_date = models.DateField(null=False)

    # def __str__(self):
    #     return self.food_name
