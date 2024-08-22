from django.shortcuts import render

app_name = 'customers'
def accounts(request):
    context={
        'title':"Red Store|Sign in or create account"

    }
    return render(request,'account.html',context=context)
def cart(request):
    context={
        'title':"Red Store|My Cart"

    }
    return render(request,'cart.html',context=context)