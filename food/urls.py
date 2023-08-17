from django.urls import path
from food import views

app_name = 'food'

urlpatterns = [
    
    path('', views.index, name='index'), # url ---> /food/
    path('<int:item_id>',views.detail, name='detail'), # url ---> /food/1
    path('add',views.create_item,name='create_item'),   # url ---> /food/add
    path('update/<int:id>',views.update_item,name='update_item'),   # url ---> /food/update/1
    path('delete/<int:id>',views.delete_item,name='delete_item'),   # url ---> /food/delete/1
]