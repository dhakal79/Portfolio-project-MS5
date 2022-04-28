from django.shortcuts import render
from .models import Service

# Create your views here.
def all_products(request):
    """A view to show all products including sorting and search results"""

    services = Service.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'service/service.html', context)
