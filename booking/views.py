from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from .forms import BookingForm

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
Date: {form.cleaned_data['traveldate']}
Destination: {form.cleaned_data['destination']}
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
