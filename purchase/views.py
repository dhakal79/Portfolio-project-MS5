from django.shortcuts import render, redirect
from django.contrib import messages
from service.models import Service

# Create your views here.

def view_purchase(request):
    """ A view that renders the purchase contents page """

    return render(request, 'purchase/purchase.html')

def add_to_purchase(request, item_id):
    """ Add a quantity of the specified service to the shopping bag """
    service = Service.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    purchase = request.session.get('purchase', {})

    if item_id in list(purchase.keys()):
        purchase[item_id] += quantity
    else:
        purchase[item_id] = quantity
        messages.success(request, f'Added {service.name} to your purchase')

    request.session['purchase'] = purchase
    return redirect(redirect_url)
    