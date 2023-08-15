from django.urls import path
from food import views

urlpatterns = [
    path('', views.index, name='index'),
]