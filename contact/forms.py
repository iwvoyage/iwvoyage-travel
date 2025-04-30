from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control'})
    )
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Your Phone Number', 'class': 'form-control'})
    )
    travel_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Destination', 'class': 'form-control'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Message', 'class': 'form-control', 'rows': 7})
    )




# ✅ New Booking Form

SERVICE_CHOICES = [
    ('vacation_package', 'Vacation Package'),
    ('cruises', 'Cruises'),
    ('train', 'Train'),
    ('flight', 'Flight'),
    ('guidedtour', 'Guided Tour'),
    ('city_train', 'City Train'),
    ('hotels', 'Hotels'),
    ('airport_transport', 'Airport Transport'),
    ('other', 'Other'),
]



SERVICE_CHOICES = [
    ('Vacation Package', 'Vacation Package'),
    ('Cruises', 'Cruises'),
    ('Train', 'Train'),
    ('Flight', 'Flight'),
    ('Guided Tour', 'Guided Tour'),
    ('City Train', 'City Train'),
    ('Hotels', 'Hotels'),
    ('Airport Transport', 'Airport Transport'),
    ('Other', 'Other'),
]

class BookingForm(forms.Form):
    name = forms.CharField(max_length=100)
    number_travelers = forms.IntegerField()
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    leaving_from = forms.CharField(max_length=100)
    destination = forms.CharField(max_length=100)
    departure_date = forms.DateField()
    return_date = forms.DateField()
    budget = forms.CharField(max_length=100)
    services = forms.MultipleChoiceField(choices=SERVICE_CHOICES, widget=forms.CheckboxSelectMultiple)
    message = forms.CharField(widget=forms.Textarea)
