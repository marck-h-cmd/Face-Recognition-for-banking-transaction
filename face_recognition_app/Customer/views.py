from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from .form import CustomUserCreationForm

# Create your views here.
@login_required
def login1(request):
    return redirect('menu')

def logout1(request):
    logout(request)
    return redirect('menu')

def register(request):
    data={
        'form':CustomUserCreationForm()
    }
    if request.method=='POST':
        user_creation_form=CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user=authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request,user)
            return redirect('menu')
    return render(request, 'register.html', data)