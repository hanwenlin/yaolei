from django.contrib import admin
from django.urls import path,include
from issues import views

app_name='issues'
urlpatterns = [
    path('', views.index,name='index'),
    path('search/',views.search,name='search'),
    path('addtion/',views.addtion,name='addtion'),
    path('modifys/<int:issueid>',views.modifys,name='modifys'),
]