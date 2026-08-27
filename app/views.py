from django.shortcuts import render
from .utils import paginate


def index(request):
    questions = []
    for i in range(1, 30):
        questions.append({
            'id': i,
            'title': f'Заголовок вопроса {i}',
            'text': f'Текст вопроса номер {i}...',
        })
    page = paginate(questions, request, per_page=5)
    return render(request, 'index.html', {'page': page})

def hot(request):
    return render(request, 'hot.html')

def tag(request, tag_name):
    return render(request, 'tag.html', {'tag_name': tag_name})

def question(request, question_id):
    return render(request, 'question.html', {'question_id': question_id})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def ask(request):
    return render(request, 'ask.html')


# Create your views here.
