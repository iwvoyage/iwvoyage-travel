from django.urls import path
from . import views

app_name = 'mediahub'

urlpatterns = [
    path('', views.mediahub_home, name='mediahub_home'),
]
