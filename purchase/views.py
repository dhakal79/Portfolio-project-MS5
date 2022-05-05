from django.shortcuts import render

# Create your views here.

def view_purchase(request):
    """ A view that renders the purchase contents page """

    return render(request, 'purchase/purchase.html')
    