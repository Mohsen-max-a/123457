from django.contrib import admin
from django.urls import path
from django.contrib.auth import views 

from . import views 

urlpatterns = [
     path("", views.game, name = "game"),
     path("login/", views.user_names, name="login"),
     path("upload_photo/", views.upload_photo, name="upload_photo"),
     path("photos/",views.photo_list, name="photo_list"),
     path("finish/", views.finish, name="finish"),
     path("search/", views.serach_users, name="search_users"),
]