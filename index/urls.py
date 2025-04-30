from django.urls import path
from .views import home, gallery_view  # 👈 import the gallery view

urlpatterns = [
    path('', home, name='home'),
    path('gallery/', gallery_view, name='gallery'),  # 👈 now this route is live
]
