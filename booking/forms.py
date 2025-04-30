from django import forms

class BookingForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    traveldate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    destination = forms.CharField(widget=forms.Textarea)
    message = forms.CharField(widget=forms.Textarea)
