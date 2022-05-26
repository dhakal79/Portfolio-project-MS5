from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from service.models import Service


def purchase_contents(request):

    purchase_items = []
    total = 0
    service_count = 0
    purchase = request.session.get('purchase', {})

    for service_id, quantity in purchase.items():
        service = get_object_or_404(Service, pk=service_id)
        total += quantity * service.price
        service_count += quantity
        purchase_items.append({
            'service_id': service_id,
            'quantity': quantity,
            'service': service,
        })

    grand_total = total

    context = {
        'purchase_items': purchase_items,
        'total': total,
        'service_count': service_count,
        'grand_total': grand_total,
    }

    return context
