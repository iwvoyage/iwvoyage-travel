from django.http import JsonResponse
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import ContactForm, BookingForm

# Contact Page View
def contact_page_view(request):
    return render(request, 'contact/contact.html')

# Contact Form Submission (AJAX)
@csrf_exempt
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            send_mail(
                subject=f"New Inquiry: {data['subject']}",
                message=f"""
Name: {data['name']}
Email: {data['email']}
Phone: {data['phone']}
Travel Date: {data['travel_date']}
Message: {data['message']}
""",
                from_email='luis@iwvoyage.com',
                recipient_list=['luis@iwvoyage.com'],
                fail_silently=False,
            )
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'message': 'Invalid request'})

# Optional: Separate contact submit endpoint
@csrf_exempt
def contact_form_submit(request):
    return contact_view(request)

# Booking Form Page
def booking_page_view(request):
    return render(request, 'contact/booking.html')

# Booking Form Submission (AJAX)
@csrf_exempt
def booking_form_view(request):
    if request.method == 'POST':
        print("📥 Booking form submitted:")
        print(request.POST)  # <-- Added to debug form data

        form = BookingForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            services_selected = ", ".join(request.POST.getlist('services'))

            message = f"""
New Booking Request

Name: {data['name']}
Email: {data['email']}
Phone: {data['phone']}
Leaving From: {data['leaving_from']}
Destination: {data['destination']}
Departure Date: {data['departure_date']}
Return Date: {data['return_date']}
Number of Travelers: {data['number_travelers']}
Budget: {data['budget']}
Services: {services_selected}

Message:
{data['message']}
"""

            send_mail(
                subject=f"Booking Request from {data['name']}",
                message=message,
                from_email='luis@iwvoyage.com',
                recipient_list=['luis@iwvoyage.com'],
                fail_silently=False,
            )
            return JsonResponse({'success': True})
        else:
            print("❌ Booking form invalid:", form.errors)
            return JsonResponse({'success': False, 'errors': form.errors})

    return JsonResponse({'success': False, 'message': 'Invalid request'})
