from django.shortcuts import render

# Create your views here.
from .models import Item, Customer, Price, SellingInfo

# def item_search(request):
#     if 'query' in request.GET:
#         query = request.GET['query']
#         items = Item.objects.filter(name__icontains=query)
#     else:
#         items = Item.objects.all()
#     return render(request, 'item_search.html', {'items': items})

def customer_search(request):
    if 'query' in request.GET:
        query = request.GET['query']
        customer = Customer.objects.filter(name__icontains=query)
    else:
        customer = Customer.objects.all()
    return render(request, 'customer_search.html', {'customer': customer})

def price_search(request):
    if 'query' in request.GET:
        query = request.GET['query']
        price = Price.objects.filter(company__icontains=query)
    else:
        price = Price.objects.all()
    return render(request, 'price_search.html', {'price': price})

def selling_search(request):
    if 'query' in request.GET:
        query = request.GET['query']
        selling = SellingInfo.objects.filter(date__icontains=query)
    else:
        selling = SellingInfo.objects.all()
    return render(request, 'selling_search.html', {'selling': selling})