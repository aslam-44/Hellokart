from django.shortcuts import render

# view for root url
app_name = 'products'
def index(request):
    context={
        'title':"Red Store|Shop swiftly"
    }
    return render(request,'index.html',context=context)
def product_details(request):
    context={
        'title':"Red Store|Product Details"

    }
    return render(request,'product_details.html',context=context)
def all_products(request):
    context={
        'title':"Red Store|All Products"

    }
    return render(request,'products.html',context=context)