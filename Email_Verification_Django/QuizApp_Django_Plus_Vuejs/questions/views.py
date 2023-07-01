from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json

# Create your views here.
def home(request):
    courses = Course.objects.all()
    context = {"courses":courses}
    return render(request,'home.html',context)

@login_required(login_url='/auth/login')
def take_quiz(request,id):
    context = {"id" : id}
    return render(request,'quiz.html',context)

def api_questions(request,id):
    raw_questions = Questions.objects.filter(course__id__contains = id)[:20]
    questions = []
    for raw_question in raw_questions:
        question = {}
        question['question'] = raw_question.question
        question['answer'] = raw_question.answer
        options = []
        options.append(raw_question.option_one)
        options.append(raw_question.option_two)
        if raw_question.option_three != '':
            options.append(raw_question.option_three)

        if raw_question.option_four != '':
            options.append(raw_question.option_four)
        
        question['options'] = options
        question['marks'] = raw_question.marks
        questions.append(question)

    return JsonResponse(questions,safe =False)

@login_required(login_url='/auth/login')
def score_page(request):
    user = request.user
    score_board = ScoreBoard.objects.filter(user = user)
    context = { 'score' : score_board }
    return render(request,'score.html',context)

@csrf_exempt
@login_required(login_url='/auth/login')
def check_marks(request):
    data = json.loads(request.body)
    quiz_answer = data.get('ques_data')
    course_id = data.get('courseId')
    user = request.user
    solutions = json.loads(quiz_answer)
    find_course = Course.objects.filter(id = course_id).first()
    score = 0
    for solution in solutions:
        question = Questions.objects.filter(question = solution.get('question')).first()
        
        if question.answer == solution.get('option'):
            score += question.marks
    
    score_card = ScoreBoard(course = find_course,user = user, score = score)
    score_card.save()
    return JsonResponse({'message':'success','status':200})

    
