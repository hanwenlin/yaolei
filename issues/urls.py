from django.contrib import admin
from django.urls import path,include
from issues import views

app_name='issues'
urlpatterns = [
    path('', views.index,name='index'),
]