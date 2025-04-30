from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

# ✅ Sitemaps
from .sitemaps import PostSitemap, DestinationSitemap, CitySitemap, DealSitemap

sitemaps = {
    'posts': PostSitemap,
    'destinations': DestinationSitemap,
    'cities': CitySitemap,
    'deals': DealSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),

    # App routes
    path('', include('index.urls')),
    path('posts/', include('post.urls')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('destinations/', include('destinations.urls', namespace='destinations')),
    path('cities/', include('cities.urls', namespace='cities')),
    path('service/', include('service.urls', namespace='service')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('process/', include('process.urls')),
    path('about/', include('about.urls')),
    path('partners/', include('partners.urls')),
    path('qna/', include('qna.urls', namespace='qna')),
    path('ads/', include('adbanner.urls', namespace='adbanner')),
    path('booking/', include('booking.urls', namespace='booking')),
    path('deals/', include('deals.urls', namespace='deals')),
    path('mediahub/', include('mediahub.urls', namespace='mediahub')),

    # SEO + Sitemap
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # Google Site Verification
    path(
        'googleRjiNSb8wJt7lpi1atZdtxpf2kvK_-Cnxsr7TqJLlJp8.html',
        TemplateView.as_view(template_name="googleRjiNSb8wJt7lpi1atZdtxpf2kvK_-Cnxsr7TqJLlJp8.html"),
        name='google-site-verification'
    ),
]

# Serve media in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
