from django.shortcuts import render
from .forms import *

# Create your views here.

def brouillon(request):

    context={}

    return render(request,'brouillon.html',context)
# Vue Welcome
def welcome(request):
    context={}

    return render(request,'welcome.html',context)

def index(request):
    context={}

    return render(request,'index.html',context)

def about(request):
    context={}

    return render(request,'about.html',context)

def price(request):
    context={}

    return render(request,'price.html',context)

def house(request):
    context={}

    return render(request,'house.html',context)

def contact(request):
    context={}

    return render(request,'contact.html',context)