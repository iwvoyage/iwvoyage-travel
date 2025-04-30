# cities/urls.py

from django.urls import path
from . import views

app_name = 'cities'

urlpatterns = [
    path('<slug:destination_slug>/', views.city_list, name='city_list'),
    path('<slug:destination_slug>/<slug:city_slug>/', views.city_detail, name='city_detail'),
]
