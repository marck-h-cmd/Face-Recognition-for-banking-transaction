from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.menu, name='menu'),
    path('customer/', include('Customer.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
