from . import views
from django.urls import path

urlpatterns = [

    path('register', views.register, name='register'),
    path('start',views.start,name='start'),
    path('logout',views.logout,name='logout')



]
