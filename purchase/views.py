from django.shortcuts import render, redirect

# Create your views here.

def view_purchase(request):
    """ A view that renders the purchase contents page """

    return render(request, 'purchase/purchase.html')

def add_to_purchase(request, item_id):
    """ Add a quantity of the specified service to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    purchase = request.session.get('purchase', {})

    if item_id in list(purchase.keys()):
        purchase[item_id] += quantity
    else:
        purchase[item_id] = quantity

    request.session['purchase'] = purchase
    print(request.session['purchase'])
    return redirect(redirect_url)
    