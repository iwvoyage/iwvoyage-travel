from django.urls import path
from . import views

app_name = 'adbanner'

urlpatterns = [
    path('', views.ad_list_view, name='ad_list'),
]
