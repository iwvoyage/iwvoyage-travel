# about/views.py
from django.shortcuts import render
from .models import AboutPage
from adbanner.models import AdBanner  # 👈 Import the model
from index.models import Trend  # or whatever your model is called
from post.models import Category, Tag

def about_page_view(request):
    about = AboutPage.objects.first()  # Assumes one about page
    categories = Category.objects.all()
    tags = Tag.objects.all()
    banners = AdBanner.objects.all()
    trends = Trend.objects.all()[:5]
    return render(request, 'about/about.html', {
        'about': about,
        'banners': banners,
        'trends': trends,
        'tags': tags,
        'categories':categories
    })
