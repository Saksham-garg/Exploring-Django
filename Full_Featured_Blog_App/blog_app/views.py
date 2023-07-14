from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2018'
#     }
# ]
@login_required(login_url='login')
def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'blog_app/home.html',context)

def about(request):
    return render(request,'blog_app/about.html')

