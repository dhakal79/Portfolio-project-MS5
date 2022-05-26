from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from service.models import Service

# Create your views here.


def view_purchase(request):
    """ A view that renders the purchase contents page """

    return render(request, 'purchase/purchase.html')


def add_to_purchase(request, service_id):
    """ Add a quantity of the specified service to the shopping bag """
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    purchase = request.session.get("purchase", {})

    if service_id in list(purchase.keys()):
        purchase[service_id] += quantity
    else:
        purchase[service_id] = quantity

    request.session["purchase"] = purchase
    return redirect(redirect_url)     
    

def adjust_purchase(request, service_id):
    """
    Change the quantity of the selected service in the shopping cart.
    """

    quantity = int(request.POST.get("quantity"))
    purchase = request.session.get("purchase", {})

    if quantity > 0:
        purchase[service_id] = quantity
    else:
        del purchase[service_id]

    request.session["purchase"] = purchase
    return redirect(reverse("view_purchase"))


def remove_from_purchase(request, service_id):
    """
    Remove the selected service from the shopping cart.
    """

    purchase = request.session.get("purchase", {})

    del purchase[service_id]

    request.session["purchase"] = purchase
    return HttpResponse(status=200)

