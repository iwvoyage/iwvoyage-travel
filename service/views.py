from django.shortcuts import render
from .models import ServicePage

def service_page(request):
    service_page = ServicePage.objects.first()  # get the first record, not a list
    return render(request, 'service/service_page.html', {'service_page': service_page})
