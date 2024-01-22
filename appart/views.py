from django.shortcuts import render

# Create your views here.


# Vue Welcome
def welcome(request):
    context={}

    return render(request,'welcome.html',context)
def index(request):
    context={}

    return render(request,'index.html',context)