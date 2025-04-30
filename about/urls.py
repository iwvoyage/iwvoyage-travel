# about/urls.py
from django.urls import path
from .views import about_page_view

app_name = 'about'

urlpatterns = [
    path('', about_page_view, name='about_page'),
]
