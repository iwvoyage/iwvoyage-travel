from django.shortcuts import render
from .models import AdBanner

def ad_list_view(request):
    banners = AdBanner.objects.all()
    return render(request, 'adbanner/ad_list.html', {'banners': banners})
