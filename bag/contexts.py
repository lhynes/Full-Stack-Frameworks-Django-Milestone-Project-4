from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    adventure_count = 0

    context = {
        'bag_items': bag_items,
        'total': total,
        'adventure_count': adventure_count,
    }

    return context
