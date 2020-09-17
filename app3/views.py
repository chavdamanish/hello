from django.contrib import auth
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        x = auth.authenticate(username=username1, password=password1)
        if x is None:
            return redirect('login')
        else:
            return redirect('/')
    else:
        return render(request, 'login.html')