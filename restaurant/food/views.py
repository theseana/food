from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from food.forms import FoodForm
from food.models import Food


@login_required
def create_food(request):
    if request.method == "POST":
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FoodForm()
            return render(request, 'food/create_food.html', {'form': form})
    else:
        form =FoodForm()
        return render(request, 'food/create_food.html', {'form': form})


def view_foods(request):
    foods = Food.objects.all()
    return render(request, 'food/view_foods.html', {'foods': foods})
