from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'portfoliov2'

urlpatterns = [
	path('', views.index, name="index"),
]	
