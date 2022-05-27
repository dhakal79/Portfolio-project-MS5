from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Service, Category
from .forms import ProductForm
from django.views.decorators.http import require_http_methods

# Views to display all the services.


def all_products(request):
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
                return redirect(reverse('service'))

        queries = Q(name__icontains=query) | Q(blurb__icontains=query)
        services = services.filter(queries)

    context = {
        'services': services,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'service/service.html', context)

# Views to display the service detail page for each service.


def product_detail(request, service_id):
    service = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'service/product_detail.html', context)

# Views to add  the service to the purchase list.


@login_required
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site manager can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save()
            messages.success(request, 'Successfully added the service!')
            return redirect(reverse('product_detail', args=[service.id]))
        else:
            messages.error(request, 'Service has not been added. Please ensure the form is valid and try again.')
    else:
        form = ProductForm()

    template = 'service/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

# Views to edit the added  the service to the purchase list.


@login_required
def edit_product(request, service_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site manager can do that.')
        return redirect(reverse('home'))

    service = get_object_or_404(Service, pk=service_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the service!')
            return redirect(reverse('product_detail', args=[service.id]))
        else:
            messages.error(request, 'Service has not been added. Please ensure the form is valid and try again.')
    else:
        form = ProductForm(instance=service)
        messages.info(request, f'You are editing {service.name}')

    template = 'service/edit_product.html'
    context = {
        'form': form,
        'service': service,
    }

    return render(request, template, context)

# Views to delete the added  the service to the purchase list.


@login_required
def delete_product(request, service_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site manager can do that.')
        return redirect(reverse('home'))

    service = get_object_or_404(Service, pk=service_id)
    service.delete()
    messages.success(request, 'Service deleted!')
    return redirect(reverse('service'))
