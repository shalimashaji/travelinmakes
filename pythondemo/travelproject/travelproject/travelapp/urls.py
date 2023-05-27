from . import views
from django.urls import path

urlpatterns = [

    path('', views.demo, name='fan'),
    path('login', views.login, name='login'),
    #  path('')

]
