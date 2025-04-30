from django.urls import path
from .views import booking_form, test_mailjet_view

app_name = 'booking'

urlpatterns = [
    path('submit/', booking_form, name='booking_form'),
    path('test-mailjet/', test_mailjet_view, name='test_mailjet'),
]
