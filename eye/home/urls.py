
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse
from home.views import home, appplication, saveFeedback, signUp,logout,login, about





urlpatterns = [
    path('', home),
    path('app', appplication),
    path('saveFeedback', saveFeedback, name='saveFeedback'),
    path('signup', signUp, name='signUp'),
    path('login', login, name='login'),
    path('logout/', logout, name='logout'),
    path('about/', about, name='about'),

]
