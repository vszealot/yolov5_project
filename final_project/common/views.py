from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, User_infoForm
from django.contrib.auth.models import User
from .models import User_info


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        info = User_infoForm(request.POST)
        print(info.is_valid())
        if form.is_valid() and info.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인

            # info.username = username
            info.username2 = request.POST["username"]
            info.height = request.POST["height"]
            info.gender = request.POST["gender"]
            info.weight = request.POST["weight"]
            info.age = request.POST["age"]
            info.save()

            user_obj = get_object_or_404(User, username=username)
            info_obj = get_object_or_404(User_info, username2="default")
            info_obj.username2 = request.POST["username"]
            info_obj.username = user_obj
            info_obj.save()

            return redirect('/main/')
    else:
        form = UserForm()
        info = User_infoForm()
    return render(request, 'common/signup.html', {'form': form, 'info' : info})