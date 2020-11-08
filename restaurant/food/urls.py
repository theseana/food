from django.urls import path

from food import views


urlpatterns = [
    path('create/', views.create_food, name="create_food"),
    path('all/', views.view_foods, name="view_food"),
]