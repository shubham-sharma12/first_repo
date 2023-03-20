from django.shortcuts import render
from store.models import *
from django.views import View

class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_product_by_id(ids)
        print(product)
        return render(request, 'cart.html', {'products': products})