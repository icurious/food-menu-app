from django.urls import path
from food import views

urlpatterns = [
    # After url ---> /food/
    path('', views.index, name='index'),
    path('<int:item_id>',views.detail, name='detail')
]