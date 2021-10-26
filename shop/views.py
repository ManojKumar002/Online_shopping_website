from django.db.models.fields import CommaSeparatedIntegerField
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib import messages
from math import ceil


from E_Commerce.settings import MEDIA_ROOT
from shop.models import Product
from shop.models import Contact
from shop.models import Checkout, Tracker


def index(request):
    allProds = []
    catprods = Product.objects.values('category')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, "shop/index.html", params)


def about(request):
    messages.success(request, 'Profile details updated.')
    return render(request, "shop/about.html")


def tracker(request):
    return render(request, "shop/tracker.html")


def checkout(request):
    success1 = {'success': False}
    if(request.method == "POST"):
        name = request.POST.get('name') #instead can use request.POST['name'] 
        email = request.POST.get('email')
        address = request.POST.get('address1')+" "+request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        phoneNumber = request.POST.get('phone')
        productJson = request.POST.get('itemsJson')
        checkout = Checkout(name=name, email=email, address=address, city=city, state=state,
                            zip_code=zip_code, phoneNumber=phoneNumber, productJson=productJson)
        checkout.save()
        orderTracker = Tracker(order_id=checkout.order_id,
                               desc="Order has been placed")
        orderTracker.save()
        success1 = {'success': True}
    return render(request, "shop/checkout.html", success1)


def contact(request):
    if(request.method == "POST"):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneNumber = request.POST.get('phoneNumber')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email,
                          phoneNumber=phoneNumber, desc=desc)
        contact.save()
    return render(request, "shop/contact.html")


def productView(request, myid):
    products = Product.objects.filter(id=myid)
    print(products)
    params = {'product': products[0]}
    return render(request, "shop/productView.html", params)

def keymatch(item,key):
    if key.lower() in item.product_name.lower() or key in item.category.lower() or key in item.subcategory.lower() or key in item.desc.lower():
        return True
    else:
        False

def search(request):
    key=request.POST.get('search')
    allProds = []
    catprods = Product.objects.values('category')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod=[item for item in prodtemp if keymatch(item,key) ]
        n = len(prod)
        if(n==0):
            continue
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, "shop/index.html", params)


def signup(request):
    if(request.method=='POST'):
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        newUser=User.objects.create_user(username,email,pass1)
        newUser.first_name=fname
        newUser.last_name=lname
        newUser.save()
        return redirect('shopHome')
    else:
        return HttpResponse('Not Found')
