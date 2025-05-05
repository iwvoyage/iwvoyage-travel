from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'name',
            'email',
            'phone',
            'leaving',
            'destination',
            'travel_date',         # <-- ✅ no trailing space
            'travel_date_end',
            'number_of_travelers',
            'message'
        ]
        widgets = {
            'travel_date': forms.DateInput(attrs={'type': 'date'}),
            'travel_date_end': forms.DateInput(attrs={'type': 'date'}),
        }
