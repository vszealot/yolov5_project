from django.shortcuts import render

# Create your views here.
def sns_main(request):
    return render(request, 'sns/share_sns.html', {'datas': '1'})

def calorie_main(request):
    return render(request, 'calorie/calorie_page.html', {'datas': '1'})