from django.urls import path
from . import views
app_name = 'products'

urlpatterns = [
    path('',views.index,name='index'),
    path('product-detail/',views.product_details,name='product_details'),
     path('all-products/',views.all_products,name='all_products'),
]