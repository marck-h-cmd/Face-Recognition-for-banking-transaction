from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
@login_required
def login(request):
    return redirect('menu')

def logout1(request):
    logout(request)
    return redirect('menu')