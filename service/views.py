from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Service, Category

# Create your views here.
def all_products(request):
    """A view to show all products including sorting and search results"""

    services = Service.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            services = services.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('services'))
            
            queries = Q(name__icontains=query) | Q(blurb__icontains=query)
            services = services.filter(queries)


    context = {
        'services': services,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'service/service.html', context)


def product_detail(request, service_id):
    """A view to show product details"""

    service = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'service/product_detail.html', context)
