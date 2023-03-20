from django.shortcuts import render
from store.models import *
from django.views import View
from store.middleware.auth import auth_Middleware

class OrderView(View):
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print('order',orders)

        return render(request, 'orders.html', {'orders':orders})