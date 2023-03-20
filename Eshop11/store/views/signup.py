from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from store.models import *
from django.views import View

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        value = {
                'first_name' : first_name,
                'last_name' : last_name,
                'phone' : phone,
                'email' : email
        }
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        error_msg = self.validateCustomer(customer)

        if not error_msg:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
            
        else:
            data = {
                'error' : error_msg,
                'values' : value
            }
            print(value)
            return render(request, 'signup.html', data)
        
    # validation
    def validateCustomer(self, customer):
        error_msg = None
        if not customer.first_name:
            error_msg = "first name required "
        elif not len(customer.first_name) > 4:
            error_msg = "must be enter 5 letters"
        elif not customer.last_name:
            error_msg = "last name required"
        elif not len(customer.last_name) > 4:
            error_msg = "last name : enter 5 or more char"
        elif not customer.phone:
            error_msg = "phone required "
        elif not len(customer.phone) > 10:
            error_msg = "phone: enter 10 char"
        elif not customer.email:
            error_msg = "required email"
        elif not len(customer.email) > 4:
            error_msg = "must be enter four letters"
        elif not len(customer.password) > 6:
            error_msg = "password : must be enter 6 letters"
        elif customer.isExist():
            error_msg = "email is already exist"
        return error_msg
