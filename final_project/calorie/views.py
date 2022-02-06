from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from camera.models import MealInfo, FoodInfo
# from common.models import User_info
from datetime import datetime
# from ..camera.models import MealInfo, FoodInfo


# Create your views here.
def calorie_main(request):
    return render(request, 'calorie/calorie_page.html')


@api_view(['GET', 'POST'])
def get_calorie_info(request):
    # 서버에서 받은 데이터 확인
    print(request.data)

    # 유저 ID 추출
    my_user = request.data['username'].split(' ')[0]

    # DB의 Date type과 비교하기 위하여 문자열 타입을 데이트 타입으로 변환
    dateString = request.data['calorie_date'].replace('/', '-')
    dateFormatter = '%m-%d-%Y'
    calorie_date = datetime.strptime(dateString, dateFormatter).date()

    # 음식 정보 추출
    food_info = FoodInfo.objects.prefetch_related('mealinfo').filter(mealinfo__username=my_user,
                                                                     mealinfo__pub_date=calorie_date)
    # 사용자 정보 추출
    meal_info = MealInfo.objects.filter(username=my_user, pub_date=calorie_date)
    food_info = food_info.values()
    meal_info = meal_info.values()
    my_food = list()

    # DB에서 받아온 정보를 Join
    for index in range(len(meal_info)):
        my_food.append({"food_name": food_info[index]['food_name'], "calorie": food_info[index]['calorie'],
                        "food_img": meal_info[index]['output_object_id'], "pub_time": meal_info[index]['pub_time']})

    context = {'dataset': my_food}
    # print('*'*100)
    print(context)
    return JsonResponse(context)
