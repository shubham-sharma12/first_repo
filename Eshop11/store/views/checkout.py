from django.shortcuts import render, redirect
from store.models import *
from django.views import View

class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_product_by_id(list(cart.keys()))
        print(phone, address, customer, cart, products)
        # print(request.POST)
        
        for product in products:
            print(cart.get(str(product.id)))
            print('customer', Customer(id=customer))
            order = Order(
                address = address,
                product = product,
                phone = phone,
                customer = Customer(id = customer),
                price = product.price,
                quantity = cart.get(str(product.id))
            )

            order.PlaceOrder()
        request.session['cart'] = {}
        return redirect('cart')