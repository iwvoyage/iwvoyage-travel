from django.http import JsonResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required

from .forms import BookingForm
from .models import Booking


@staff_member_required
def booking_dashboard(request):
    bookings = Booking.objects.all().order_by('-created_at')
    return render(request, 'booking/booking_dashboard.html', {'bookings': bookings})


@csrf_exempt
def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            send_mail(
                subject="New Booking Request",
                message=f"""
Name: {form.cleaned_data['name']}
Email: {form.cleaned_data['email']}
Phone: {form.cleaned_data['phone']}
Start Date: {form.cleaned_data['travel_date']}
End Date: {form.cleaned_data['travel_date_end']}
Destination: {form.cleaned_data['destination']}
Travelers: {form.cleaned_data['number_of_travelers']}
Message: {form.cleaned_data['message']}
""",
                from_email='luis@iwvoyage.com',
                recipient_list=['luis@iwvoyage.com'],
                fail_silently=False,
            )
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'message': 'Invalid request'})


def test_mailjet_view(request):
    send_mail(
        subject='Mailjet Test',
        message='If you got this, Mailjet is working!',
        from_email='luis@iwvoyage.com',
        recipient_list=['luis@iwvoyage.com'],
        fail_silently=False,
    )
    return JsonResponse({'message': 'Test email sent!'})


def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()

            # ✅ Send email to admin
            send_mail(
                subject="New Booking Request",
                message=f"""
Name: {booking.name}
Email: {booking.email}
Phone: {booking.phone}
Start Date: {booking.travel_date}
End Date: {booking.travel_date_end}
Destination: {booking.destination}
Travelers: {booking.number_of_travelers}
Message: {booking.message}
""",
                from_email='luis@iwvoyage.com',
                recipient_list=['luis@iwvoyage.com'],
                fail_silently=False,
            )

            # ✅ Confirmation email to customer
            send_mail(
                subject="✈️ Your iwVoyage Booking Request Received!",
                message=f"""
Hi {booking.name},

Thanks for submitting your booking request to {booking.destination}!

🗓 Dates: {booking.travel_date} to {booking.travel_date_end}
👥 Travelers: {booking.number_of_travelers}

We'll follow up shortly with a custom itinerary.

– The iwVoyage Team
""",
                from_email='luis@iwvoyage.com',
                recipient_list=[booking.email],
                fail_silently=False,
            )

            return redirect('booking:booking_thank_you')
    else:
        form = BookingForm()

    return render(request, 'booking/booking_form.html', {'form': form})


def booking_thank_you(request):
    return render(request, 'booking/thank_you.html')
