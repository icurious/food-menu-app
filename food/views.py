
from re import template
from django.shortcuts import render, redirect
from food.models import Item
from django.template import loader
from food.forms import ItemForm
# Create your views here.

def index(request):
    item_list = Item.objects.all()
    context = { 'item_list': item_list }
    return render(request,'food/index.html',context)

def detail(request,item_id):
    item_detail = Item.objects.get(pk=item_id)
    context = {'item_detail': item_detail}
    return render(request,'food/detail.html',context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    context = {'form': form}

    return render(request,'food/item-form.html',context)


def update_item(request,id):
    item = Item.objects.get(pk=id)
    form = ItemForm(request.POST or None,instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    context = {'form': form, 'item': item}

    return render(request,'food/item-form.html',context)


def delete_item(request,id):
    item = Item.objects.get(pk=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    context = {'item': item}

    return render(request, 'food/delete-item.html',context)
    
    