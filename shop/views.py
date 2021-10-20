from django.db.models.fields import CommaSeparatedIntegerField
from django.shortcuts import render
from django.http.response import HttpResponse
from E_Commerce.settings import MEDIA_ROOT
from shop.models import Product
from shop.models import Contact
from math import ceil

def index(request):
    allProds=[]
    catprods= Product.objects.values('category')
    cats= { item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n= len(prod)
        nSlides= n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])
    params={'allProds':allProds }
    return render(request,"shop/index.html", params)

def about(request):
    return render(request,"shop/about.html")

def tracker(request):
    return render(request,"shop/tracker.html")

def contact(request):
    if(request.method=="POST"):
        name=request.POST.get('name')
        email=request.POST.get('email')
        phoneNumber=request.POST.get('phoneNumber')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phoneNumber=phoneNumber,desc=desc)
        contact.save()
    return render(request,"shop/contact.html")

def productView(request,myid):
    products=Product.objects.filter(id=myid)
    print(products)
    params={'product':products[0]}
    return render(request,"shop/productView.html",params)