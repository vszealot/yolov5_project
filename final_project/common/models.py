from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class User_info(models.Model):
    username = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="user", db_column="username", to_field="username")
    username2 = models.CharField("임시", null=True, max_length=150)
    gender = models.CharField("성별", max_length=1, null=True)
    height = models.IntegerField("키", null=True)
    weight = models.IntegerField("몸무게", null=True)
    age = models.IntegerField("나이", null=True)
