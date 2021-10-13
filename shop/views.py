from django.db.models.fields import CommaSeparatedIntegerField
from django.shortcuts import render
from django.http.response import HttpResponse
from E_Commerce.settings import MEDIA_ROOT
from shop.models import Product
from math import ceil

def index(request):
    products= Product.objects.all()
    n= len(products)
    nSlides= n//4 + ceil((n/4)-(n//4))
    allProds=[[products, range(1, nSlides), nSlides],[products, range(1, nSlides), nSlides]]
    params={'allProds':allProds }
    return render(request,"shop/index.html", params)

def about(request):
    return render(request,"shop/about.html")