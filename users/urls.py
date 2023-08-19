from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    
    path('', views.register_users, name='register_users'), # url ---> /register

]