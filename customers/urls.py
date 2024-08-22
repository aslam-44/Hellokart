from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('login/',views.accounts,name='accounts'),
     path('cart/',views.cart,name='cart')
]