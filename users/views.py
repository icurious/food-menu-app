from contextlib import redirect_stderr
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from users.forms import RegisterUserForm

from django.contrib.auth.decorators import login_required
# Create your views here.



def register_users(request):

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            message = "Welcome {} your Account has been created!!" .format(username)
            messages.success(request,message)
            return redirect('login')
    else:
        form = RegisterUserForm()
    
    context = {'form': form}
    return render(request,'users/register.html',context)

@login_required
def profile(request):
    return render(request,'users/profile.html')