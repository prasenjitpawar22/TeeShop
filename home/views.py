from django.shortcuts import render
from dashboard.models import Product
from django import template
import random
from django.contrib.auth.decorators import login_required


# Create your views here.
def homePage(request):
    products_list = list(Product.objects.all())     # get product list
    products = random.sample(products_list, 4)      # random 4 
    return render(request, 'home.html', {'products':products})

def productDetails(request, product_id):
    product = Product.objects.get(id=product_id)
    color_list = product.colors
    color_list = color_list.split(',')
    # print(color_list[0])
    

    return render(request, 'product_details.html', {'product': product, 'color_list': color_list})

