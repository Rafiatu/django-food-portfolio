from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Food


# Create your views here.
def index(request):
    foods = Food.objects
    return render(request, 'foods/index.html', {'foods': foods})

def detail(request, food_id):
    food_detail = get_object_or_404(Food, pk = food_id)
    return render(request, 'foods/detail.html', {'food': food_detail})