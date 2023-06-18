from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('login_attempt/',login_attempt,name='login_attempt'),
    path('register_attempt/',register_attempt,name='register_attempt'),
    path('email_token/',email_token,name='email_token'),
    path('success/',success,name='success'),
    path('error/',error,name='error'),
    path('verify/<auth_token>',verify,name='verify'),
]