from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('<id>',take_quiz,name="take_quiz"),
    path('api/<id>',api_questions,name="api_questions")
]