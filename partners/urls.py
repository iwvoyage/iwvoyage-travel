from django.urls import path
from .views import partner_list_view

app_name = "partners"

urlpatterns = [
    path('', partner_list_view, name='partner_list'),
]