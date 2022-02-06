from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User_info


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")

class User_infoForm(forms.ModelForm):
    class Meta:
        model = User_info
        fields = ("username2", "gender", "height", "weight", "age")