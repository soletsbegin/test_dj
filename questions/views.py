from django.shortcuts import render
from django.http.response import HttpResponse

from questions.models import Question


def hello(HttpRequest):
    print('rydcfghj')
    return HttpResponse('Hello')


def all_questions(request):
    questions_list = Question.objects.all()
    context = {'questions_list': questions_list}
    return render(request, 'questions/index.html', context)


def one_question(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse


def index(request):
    return HttpResponse('index')