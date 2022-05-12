from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from service.models import Service
from purchase.contexts import purchase_contents



@require_POST
def cache_checkout_data(request):
    """module string"""
    try:
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            "purchase": json.dumps(request.session.get("purchase", {})),
            "save_info": request.POST.get("save_info"),
            "username": request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, "Sorry, your payment cannot be \
            processed right now. Please try again later.")
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Renders the checkout page with the current purchase contents.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        purchase = request.session.get("purchase", {})

        form_data = {
            "full_name": request.POST["full_name"],
            "email": request.POST["email"],
            "phone_number": request.POST["phone_number"],
            "country": request.POST["country"],
            "postcode": request.POST["postcode"],
            "town_or_city": request.POST["town_or_city"],
            "street_address1": request.POST["street_address1"],
            "street_address2": request.POST["street_address2"],
            "county": request.POST["county"],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get("client_secret").split("_secret")[0]
            order.user = request.user.username
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()

            for service_id, quantity in purchase.items():
                service = get_object_or_404(Service, pk=service_id)
                order_line_item = OrderLineItem(
                    order=order,
                    service=service,
                    quantity=quantity,
                )
                order_line_item.save()
            request.session["save_info"] = "save-info" in request.POST
            return redirect(
                reverse(
                    "checkout_success",
                    args=[
                        order.order_number]))
        else:
            messages.error(request, "There was an error with your form. \
                Please double check your information.")

    else:
        purchase = request.session.get("purchase", {})
        if not purchase:
            messages.error(
                request, "There's nothing in your purchase! Redirecting...")
            return redirect(reverse("service"))

        current_purchase = purchase_contents(request)
        total = current_purchase['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(
            request,
            "Stripe public key is missing, check that it's set in the enviornment!")

    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handles successful checkouts
    """
    save_info = request.session.get("save_info")
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if "purchase" in request.session:
        del request.session["purchase"]

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
    }

    return render(request, template, context)
