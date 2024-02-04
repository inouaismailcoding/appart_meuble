from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from .forms import *
from .forms import AddressForm
from .models import PropertyType,Property
# Create your views here.


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

def list_property(request):

    return render(request,'list_property.html')

def add_property(request):
    if request.method == 'POST':
        property_form = PropertyForm(request.POST)
        details_form = None
        if property_form.is_valid():
            
            property = property_form.save(commit=False)
            type_property = property_form.cleaned_data['property_type']
            print(type_property)
            if type_property == 1:
                details_form = AppartementDetailsForm(request.POST)
                
            elif type_property == 2:
                details_form = DuplexDetailsForm(request.POST)
            elif type_property == 3:
                details_form = ImmeubleDetailsForm(request.POST)

            if details_form and details_form.is_valid():
                property.save()
                details = details_form.save(commit=False)
                details.property = property
                details.save()
                return redirect('list_property')  # Rediriger vers la page d'accueil ou toute autre vue après l'ajout
    
    else:
        context={}
        if request.method == 'GET' and 'add_detail_property' in request.GET :
            type_property=request.GET['id_property_type']
            if type_property == '1':
                form=AppartementDetailsForm()
            elif type_property == '2':
                form = DuplexDetailsForm()
            elif type_property == '3':
                form = ImmeubleDetailsForm()
            else:
                form = None
        
            if form:
                context['form'] = form.as_p()
                return JsonResponse(context)
        context['PropertyType']=PropertyType.objects.all().order_by('name')
        context['property_form']=PropertyForm()
        context['address_form']=AddressForm()   
        return render(request, 'add_property.html', context)

def photo(request):
    if request.method == 'POST':
        print(request.POST)
        form = PhotoForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('add_property')
    else:
        form = PhotoForm()
    return render(request, 'photo.html', {'form': form})
def detail_property(request):

    return render(request,'detail_property.html')


