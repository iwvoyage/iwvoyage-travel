from django.urls import path
from . import views


app_name = 'process'

urlpatterns = [
    path('', views.process_view, name='process'),
]
