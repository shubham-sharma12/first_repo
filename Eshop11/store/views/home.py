from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from store.models import *
from django.views import View

# Create your views here.
class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        print('product', product)
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        # print(request.GET)
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_product_by_categoryid(categoryID)
        else:
            products = Product.get_all_product()
        # print('id:', categoryID)
        data = {}
        data['products'] = products
        data['categories'] = categories
        # print(categories)
        # return HttpResponse("<h1>index page</h1>")
        print(request.session.get('customer_email'))
        return render(request, 'index.html', data)
