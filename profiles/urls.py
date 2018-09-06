from django.urls import path
from django.contrib import admin

from profiles import views

urlpatterns = [
    path('',           views.home,         name='home'),
    path('about/',     views.about,        name='about'),
    path('albums/',    views.albums,       name='albums'),
    path('songs/',     views.songs,        name='songs'),
    
    #hii hapa 
    path('newalbum/',  views.addalbum,     name='addalbum'),
    path('add/',       views.add,          name='add')
]