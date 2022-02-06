from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from camera.models import MealInfo
from datetime import datetime
from collections import Counter


# Create your views here.
def main(request):
    return render(request, 'main/main.html')

@api_view(['GET', 'POST'])
def getDatas(request):
    print("=" * 100)
    print(request.data)
    print("=" * 100)

    dateFormatter = '%m-%d-%Y'
    start_date = datetime.strptime(request.data['start_date'].replace('/', '-'), dateFormatter).date()
    end_date = datetime.strptime(request.data['end_date'].replace('/', '-'), dateFormatter).date()
    username = request.data['username']
    results = MealInfo.objects.filter(username=username, pub_date__range=[start_date, end_date]).values()

    food_name_list = []
    for result in results:
        food_name_list.append(result['food_name_id'])
    food_name_counter = Counter(food_name_list)

    food_name_count_list = []
    for key, value in food_name_counter.most_common():
        food_name_count_list.append({"menu" : key, "count" : value})

    context = {"datas" : food_name_count_list}

    return JsonResponse(context)
