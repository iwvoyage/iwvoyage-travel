from django.shortcuts import render, get_object_or_404
from .models import Destination
from adbanner.models import AdBanner  # 👈 Import the model
from index.models import Trend  # or whatever your model is called

def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'destinations/list.html', {'destinations': destinations})


def destination_detail(request, slug):
    destination = get_object_or_404(Destination, slug=slug)
    banners = AdBanner.objects.all()  # 👈 Load banners
    trends = Trend.objects.all()[:5]  # Limit to 5 or whatever you want
    return render(request, 'destinations/detail.html', {'destination': destination,'trends': trends,'banners': banners})

