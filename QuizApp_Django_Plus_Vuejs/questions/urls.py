from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('score',score_page,name="score_page"),
    path('<id>',take_quiz,name="take_quiz"),
    path('api/check',check_marks,name="check_marks"),
    path('api/<id>',api_questions,name="api_questions")
]