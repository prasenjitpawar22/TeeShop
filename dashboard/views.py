from django.shortcuts import render, redirect
from .models import Product
from .forms import (
        ProductForm,
#        CreatePageForm
)
# python standard lib
import base64
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='login')
def home_dashboard(request):
    return render(request, 'home_dashboard.html')


@login_required(login_url='login')
def create_dashboard(request):
    if request.POST.get('kids'):
    #    title = request.POST['title'] #get the title of product
        request.session['product_title'] = 'kidsT-shirt'
        print('kdis')
        return redirect('designDashboard')
    #    request.session['product_title'] = title # save the title in session variable
    
    if request.POST.get('women'):
        request.session['product_title'] = 'womensT-shirt'
        print('kdis')
        return redirect('designDashboard')
        print(v)
    
    if request.POST.get('mens'):
        request.session['product_title'] = 'mensUnisex'
        print('kdis')
        return redirect('designDashboard')
    
    if request.POST.get('unisex'):
        request.session['product_title'] = 'mensUnisex'
        print('kdis')
        return redirect('designDashboard')
     

    return render(request, 'create_dashboard.html')


@login_required(login_url='login')
def analysis_dashboard(request):
    return render(request, 'analysis_dashboard.html')


@login_required(login_url='login')
def design_view(request):
    product_title = request.session.get('product_title')
    print(product_title)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES or None)
        # if request.method == "POST":
        #     form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # form.cleaned_data['name'] = product_title
            Product = form.save(commit=False)
            Product.name = product_title
            Product.user = request.user
            print(Product.title)
            data = form.cleaned_data['mockupData']
            print(data)
            #data = data.replace("data:image/png;base64,", "")
            
            # base64 to file
            format, imgstr = data.split(';base64,')
            print("format", format)
            ext = format.split('/')[-1]
            print(ext)
            
            data = ContentFile(base64.b64decode(imgstr))  
            file_name = "'myphoto." + ext
            Product.mockupImg.save(file_name, data, save=True) # image is Product's model field
            # remove the Base64 data later 
            #form.cleaned_data['mockupData'] = ''
            # Product.save()
            print('saved')
            return redirect('createDashboard')
            
        else:
            print("invalid")
    else:
        form = ProductForm()

    return render(request, 'design_dashboard.html', {'form':form, 'product_title':product_title})


@login_required(login_url='login')
def listing_dashboard(request):

    product_list = Product.objects.all().filter(user = request.user)
    # for product in product_list:
    #     print(product.id, product.name, product.image)

    # print(product_list)

    return render(request, 'listing_dashboard.html', {'product_list':product_list})

def delete_product(request, product_id):
    object = Product.objects.get(id=product_id)
    object.delete()
    return redirect('listingDashboard')
