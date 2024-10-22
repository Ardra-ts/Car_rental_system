from django.contrib import admin
from django.urls import path
from .import views


urlpatterns =[
    path('',views.index, name='index'),
    path('car/',views.car, name='car'),
    path('contact/',views.contact, name='contact'),
    path('chat/<pk>',views.chat,name='chat'),
    path('about/',views.about, name='about')
]  