from django.urls import path
from .views import *
from . import views

app_name = "music"

urlpatterns = [
    path('', views.singer_list_create),
    path('songs', views.song_list_create),
]