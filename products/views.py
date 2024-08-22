from django.shortcuts import render

# view for root url
app_name = 'products'
def index(request):
    return render(request,'index.html')
