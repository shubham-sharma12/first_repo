from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models import *
from django.views import View
from django.contrib.auth.hashers import make_password, check_password


class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        print('running')
        return render(request, 'login.html')

    def post(self, request):
        print('posting')
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        print(customer)
        error_msg = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                request.session['customer_email'] = customer.email
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    return redirect('homepage')
            else:
                error_msg = "invalid email and password"
        else:
            error_msg = "wrong email"
        print(email, password)
        return render(request, 'login.html', {'error' : error_msg})

def logout(request):
    request.session.clear()
    return redirect('login')