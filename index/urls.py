from django.urls import path
from .views import home, gallery_view  # 👈 import the gallery view
from .views import test_s3_upload

urlpatterns = [
    path('', home, name='home'),
    path('gallery/', gallery_view, name='gallery'),  # 👈 now this route is live
    path('test-upload/', test_s3_upload, name='test_upload'),
]
