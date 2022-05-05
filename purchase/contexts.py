from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from service.models import Service


def purchase_contents(request):

    purchase_items = []
    total = 0
    service_count = 0
    purchase = request.session.get('purchase', {})

    for item_id, quantity in purchase.items():
        service = get_object_or_404(Service, pk=item_id)
        total += quantity * service.price
        service_count += quantity
        purchase_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'service': service,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    grand_total = total
    
    context = {
        'purchase_items': purchase_items,
        'total': total,
        'service_count': service_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
