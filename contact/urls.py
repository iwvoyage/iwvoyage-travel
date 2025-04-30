from django.urls import path
from .views import (
    contact_page_view,
    contact_view,
    booking_page_view,
    booking_form_view,
)

app_name = "contact"

urlpatterns = [
    path('', contact_page_view, name='contact_page'),  # /contact/
    path('submit/', contact_view, name='contact_form_submit'),  # AJAX contact form handler
    path('booking/', booking_page_view, name='booking_page'),  # /contact/booking/
    path('booking/submit/', booking_form_view, name='booking_form_submit'),  # AJAX booking form handler
]
