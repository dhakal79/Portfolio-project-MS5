from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from service.models import Service

# Views for service purchase model.


def view_purchase(request):
    """ A view that renders the purchase contents page """

    return render(request, 'purchase/purchase.html')

# function to add purchase of service


def add_to_purchase(request, service_id):
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    purchase = request.session.get("purchase", {})

    if service_id in list(purchase.keys()):
        purchase[service_id] += quantity
    else:
        purchase[service_id] = quantity

    request.session["purchase"] = purchase
    return redirect(redirect_url)

# function to edit the added purchased service


def adjust_purchase(request, service_id):
    quantity = int(request.POST.get("quantity"))
    purchase = request.session.get("purchase", {})

    if quantity > 0:
        purchase[service_id] = quantity
    else:
        del purchase[service_id]

    request.session["purchase"] = purchase
    return redirect(reverse("view_purchase"))

# function to remove the the added purchased service


def remove_from_purchase(request, service_id):
    purchase = request.session.get("purchase", {})

    del purchase[service_id]

    request.session["purchase"] = purchase
    return HttpResponse(status=200)
