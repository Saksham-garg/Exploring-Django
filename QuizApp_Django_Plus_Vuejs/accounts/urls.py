from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', auth_login,name ="login_attempt"),
    path('register/', register,name ="register_attempt"),
    path('logout/', logout_page,name ="logout_page"),
]