from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from ..forms import UserRegisterForm

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home_page') 
        else:
            print(form.errors)  
    else:
        form = UserRegisterForm()
    return render(request, 'auth/register.html', {'form': form})