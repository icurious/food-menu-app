from re import template
from django.shortcuts import render,HttpResponse
from food.models import Item
from django.template import loader
# Create your views here.

def index(request):
    item_list = Item.objects.all()
    context = { 'item_list': item_list }
    return render(request,'food/index.html',context)

def detail(request,item_id):
    item_detail = Item.objects.get(pk=item_id)
    context = {'item_detail': item_detail}
    return render(request,'food/detail.html',context)
