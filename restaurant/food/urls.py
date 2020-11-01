from django.urls import path

from food import views


urlpatterns = [
    path('create/', views.create_food, name="create_food")
]