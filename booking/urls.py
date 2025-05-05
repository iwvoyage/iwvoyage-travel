from django.urls import path
from .views import booking_view, booking_form, test_mailjet_view, booking_thank_you,booking_dashboard

app_name = 'booking'  # ✅ This line fixes the namespace error

urlpatterns = [
    path('book/', booking_view, name='book'),
    path('api/', booking_form, name='form'),
    path('test-mailjet/', test_mailjet_view, name='mailjet'),
    path('thank-you/', booking_thank_you, name='booking_thank_you'),
    path('dashboard/', booking_dashboard, name='dashboard'),

]
