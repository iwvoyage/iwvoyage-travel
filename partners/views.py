from django.shortcuts import render
from .models import Partner

def partner_list_view(request):
    categories = ['hotels', 'tours', 'airlines', 'boards']
    partners_by_category = {
        cat: Partner.objects.filter(category=cat) for cat in categories
    }
    return render(request, 'partners/partner_list.html', {
        'partners_by_category': partners_by_category
    })
