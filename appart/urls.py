from django.urls import path
from . import views

urlpatterns=[
    path('',views.welcome,name='welcome'),
    path('index',views.index,name='index'),
    path('house',views.house,name='house'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('price',views.price,name='price'),
]