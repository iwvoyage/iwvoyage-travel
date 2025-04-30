from django.shortcuts import render
from .models import Question
from index.models import Trend

def question_list(request):
    questions = Question.objects.all()
    trends = Trend.objects.all()[:5]
    return render(request, 'qna/question_list.html', {'questions': questions, 'trends': trends,})
