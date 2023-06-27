from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login,name ="login_attempt"),
    path('register/', register,name ="register_attempt"),
]