
from django.contrib import admin
from django.urls import path , include

from .import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('loggin/', views.loggin, name='loggin'),
    path('loggout/', views.loggout, name='loggout'),
    path('index/', views.index, name='index'),
    path('change_pwd/', views.change_pwd, name='change_pwd'),
    path('change_pwd1/', views.change_pwd1, name='change_pwd1'),

]
