
from django.contrib import admin
from django.urls import path
from serverApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.calculate_values, name='calculatePowerRoot')
]
