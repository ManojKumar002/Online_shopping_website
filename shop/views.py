from django.shortcuts import render
from django.http.response import HttpResponse

def index(request):
    return render(request,"shop/index.html")

def about(request):
    return render(request,"shop/about.html")