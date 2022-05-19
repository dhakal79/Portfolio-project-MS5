from django.shortcuts import render, redirect, reverse, HttpResponse
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


def adjust_purchase(request, service_id):
    """
    Change the quantity of the selected book in the shopping cart.
    """

    quantity = int(request.POST.get("quantity"))
    purchase = request.session.get("purchase", {})

    if quantity > 0:
        purchase[service_id] = quantity
    else:
        del purchase[service_id]

    request.session["purchase"] = purchase
    return redirect(reverse("purchase"))


def remove_from_purchase(request, service_id):
    """
    Remove the selected book from the shopping cart.
    """

    purchase = request.session.get("purchase", {})

    del purchase[service_id]

    request.session["purchase"] = purchase
    return HttpResponse(status=200)
