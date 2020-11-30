from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('index/',views.index,name="index"),
    path('main/', views.home,name = "main"),
    path('home/', views.home,name = "home"),
    path('box_one/', views.box_one,name = "box_one"),
    path('box_two/', views.box_two,name = "box_two"),
    path('box_three/', views.box_three,name = "box_three"),
     path('about/', views.about,name = "about"),
    path('addInForum/',views.forum,name = "addInForum"),
    path('addInDiscussion/',views.addInDiscussion,name="addInDiscussion"),
   
]