from django.urls import include, path
from . import views

urlpatterns = [
    path('login/', views.login1, name="login1"),
    path('logout/', views.logout1, name="logout1"),
    path('singin/', views.singin, name="singin"),
    path('accounts/', include('django.contrib.auth.urls')),
]