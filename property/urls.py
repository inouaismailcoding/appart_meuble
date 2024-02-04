from django.urls import path
from . import views

urlpatterns = [
    path("list_property", views.list_property, name="list_property"),
    path("", views.add_property, name="add_property"),
    path(":<id>", views.detail_property, name="detail_property"),
    path("photo",views.photo,name='photo'),
    path('',views.welcome,name='welcome'),
    path('index',views.index,name='index'),
    path('house',views.house,name='house'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('price',views.price,name='price'),
    path('brouillon',views.brouillon,name='brouillon'),
]
