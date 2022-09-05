from django.urls import path
from .views import *

urlpatterns = [
    path('create',index, name="index"),
    path('',Login, name="Login"),
    path('home',home, name="home"),
    path('classes',classes, name="classes"),
    path('update/<int:id>',updateview, name="update"),
    path('update/updaterecord/<int:id>', updaterecordview, name='updaterecord'),
    path('delete/<int:id>', deleteview, name='delete'),
]
