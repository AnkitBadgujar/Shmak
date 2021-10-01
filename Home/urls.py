from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('audio',views.audio,name='audio'),
    path('video',views.video,name='video'),
    path('photo',views.photo,name='photo'),
    path('allcontact',views.allcontact,name='allcontact')
    
]
