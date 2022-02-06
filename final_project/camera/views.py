# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
import requests
import cv2
from .models import MealInfo, FoodInfo
import json
import numpy as np
from django.contrib.auth.models import User
from datetime import datetime


def camera(request):
    if request.method == "POST":
        print(request.POST)
        context = {'input_date': request.POST['input_date'],
                   'meal': request.POST['meal']}
        return render(request, 'camera/camera.html', context)
    else:
        return render(request, 'camera/camera.html')


@api_view(['GET', 'POST'])
def get_img(request):
    # request 받은 값 정리
    username = request.data['username']
    mealtime = request.data['meal']
    inputdate = request.data['input_date'].replace("/", "")
    context = dict(request.data)

    # 경로설정
    BASE_PATH = "C:\\PythonWork\\final_project\\final_project\\static\\userResult\\"
    origin_path = f"{BASE_PATH}{username}_{inputdate}_{mealtime}_origin.jpg"
    result_path = f"{BASE_PATH}{username}_{inputdate}_{mealtime}_result.jpg"

    # api서버 주소
    DETECTION_URL = "http://3.34.244.242:5000/rest"

    # 이미지 저장
    with open(origin_path, "wb") as f:
        for chunk in request.data['image_uploads'].chunks():
            f.write(chunk)

    # 모델에 값 전달-return
    image_data = open(origin_path, "rb").read()
    response = requests.post(DETECTION_URL, files={"image": image_data}).json()
    result = response["result"]
    result_dict = json.loads(result)[0]  # 라벨값
    labels = np.asarray(response["labels"])
    cord = np.asarray(response["cord"])
    frame = cv2.imread(origin_path)

    # 원본이미지에 결과박스 그리기, 저장
    n = len(labels)
    x_shape, y_shape = frame.shape[1], frame.shape[0]
    for i in range(n):
        row = cord[i]
        if row[4] >= 0.2:
            x1, y1, x2, y2 = int(row[0] * x_shape), int(row[1] * y_shape), int(row[2] * x_shape), int(
                row[3] * y_shape)
            bgr = (0, 255, 0)
            cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 1)
            cv2.putText(frame, result_dict["name"], (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, bgr, 2)
    cv2.imwrite(result_path, frame)

    # context 전달
    context['imgsrc'] = f'/static/userResult/{username}_{inputdate}_{mealtime}_result.jpg'
    del context['csrfmiddlewaretoken']
    del context['username']
    del context['image_uploads']
    context['input_date'] = context['input_date'][0]
    context['meal'] = context['meal'][0]
    context['foodname'] = result_dict["name"]

    return render(request, 'camera/get_img.html', context)


@api_view(['GET', 'POST'])
def put_meal_info(request):
    my_food = request.data['foodname']
    if my_food == 'Sushi':
        my_food = '초밥'
    elif my_food == 'Udon':
        my_food = '우동'
    elif my_food == 'Champon':
        my_food = '짬뽕'
    elif my_food == 'Jajangmyeon':
        my_food = '짜장면'
    elif my_food == 'Fried Chicken':
        my_food = '치킨'
    elif my_food == 'Pizza':
        my_food = '피자'

    username = User.objects.get(username=request.data['username'])
    food_name = FoodInfo.objects.get(food_name=my_food)

    dateString = request.data['input_date'].replace('/', '-')
    dateFormatter = '%m-%d-%Y'
    input_date = datetime.strptime(dateString, dateFormatter).date()

    result = MealInfo.objects.filter(username=username, pub_date=input_date, pub_time=request.data['meal']).values_list('pk', flat=True)

    if result:
        item = MealInfo.objects.get(pk=result[0])
        item.delete()

    MealInfo.objects.create(username=username,
                            food_name=food_name,
                            output_object_id=request.data['imgsrc'],
                            pub_time=request.data['meal'],
                            pub_date=input_date)

    return redirect('/main/')
