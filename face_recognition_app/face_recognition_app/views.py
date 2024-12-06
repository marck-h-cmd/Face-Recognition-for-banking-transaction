from django.shortcuts import redirect, render

def menu(request):
    return render(request, 'menu.html', {})
