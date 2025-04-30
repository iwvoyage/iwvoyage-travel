from django.urls import path
from .views import question_list

app_name = 'qna'

urlpatterns = [
    path('', question_list, name='question_list'),
]
