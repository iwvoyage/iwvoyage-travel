from django.shortcuts import render
from django.utils import timezone
from .models import Deal
from index.models import Trend  # or whatever your model is called


def active_deal_view(request):
    trends = Trend.objects.all()[:5]  # Limit to 5 or whatever you want
    today = timezone.now().date()
    deal = Deal.objects.filter(
        is_active=True,
        start_date__lte=today,
        end_date__gte=today
    ).first()

    return render(request, 'deals/deal_detail.html', {'deals': deal, 'trends': trends,})
