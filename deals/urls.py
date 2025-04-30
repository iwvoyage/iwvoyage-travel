from django.urls import path
from .views import active_deal_view

app_name = 'deals'  # <-- make sure this is plural if you're using 'deals' in the url tag

urlpatterns = [
    path('', active_deal_view, name='current_deal'),  # ✅ this fixes the NoReverseMatch
]
