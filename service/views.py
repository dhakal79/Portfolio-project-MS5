from django.shortcuts import render, get_object_or_404
from .models import Service

# Create your views here.
def all_products(request):
    """A view to show all products including sorting and search results"""

    services = Service.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'service/service.html', context)


def product_detail(request, service_id):
    """A view to show product details"""

    service = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'service/product_detail.html', context)
