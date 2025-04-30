from django.contrib.sitemaps import Sitemap
from post.models import Post
from destinations.models import Destination
from cities.models import City
from deals.models import Deal  # adjust if your app is named differently

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.objects.all()

    def location(self, obj):
        return f"/posts/{obj.slug}/"


class DestinationSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Destination.objects.all()

    def location(self, obj):
        return f"/destinations/{obj.slug}/"


class CitySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return City.objects.all()

    def location(self, obj):
        return f"/destinations/{obj.destination.slug}/{obj.slug}/"


class DealSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Deal.objects.filter(is_active=True)

    def location(self, obj):
        return f"/deals/"  # Update if you use slugs or dynamic detail pages
