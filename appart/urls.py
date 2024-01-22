from django.urls import path
from . import views

urlpatterns=[
    path('',views.welcome,name='welcome'),
    path('index',views.index,name='index')
]