from django.urls import include, path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout1/', views.logout1, name="logout1"),
    path('accounts/', include('django.contrib.auth.urls')),
]