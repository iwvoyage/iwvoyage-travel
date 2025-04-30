from django.shortcuts import render, get_object_or_404
from .models import City
from destinations.models import Destination
from post.models import Post, Category, Tag  # ✅ Add Category and Tag
from adbanner.models import AdBanner  # 👈 Import the model
from index.models import Trend  # or whatever your model is called

def city_list(request, destination_slug):
    destination = get_object_or_404(Destination, slug=destination_slug)
    cities = destination.cities.all()
    return render(request, 'cities/city_list.html', {
        'destination': destination,
        'cities': cities
    })


def city_detail(request, destination_slug, city_slug):
    destination = get_object_or_404(Destination, slug=destination_slug)
    city = get_object_or_404(City, slug=city_slug, destination=destination)
    latest_posts = Post.objects.order_by('-created_at')[:4]
    banners = AdBanner.objects.all()
    trends = Trend.objects.all()[:5]
    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'cities/city_detail.html', {
        'destination': destination,
        'city': city,
        'latest_posts': latest_posts,
        'trends': trends,
        'banners': banners,
        'categories': categories,  # ✅ Add to context
        'tags': tags,              # ✅ Add to context
    })