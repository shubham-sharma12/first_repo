from .views.home import Index
from .views.login import Login, logout
from .views.signup import Signup
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from django.urls import path
from store.middleware.auth import auth_Middleware

urlpatterns = [
    path('', Index.as_view(), name ='homepage'),
    path('signup', Signup.as_view()),
    path('login', Login.as_view(), name="login"),
    path('logout', logout, name="logout"),
    path('cart', Cart.as_view(), name="cart"),
    path('check-out', CheckOut.as_view()),
    path('order', auth_Middleware(OrderView.as_view()))
]