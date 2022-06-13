from asyncio.log import logger
from django.dispatch import receiver
from django.shortcuts import render, redirect
from .models import  HomeProduct, HomeSlide,aboutus,stays,flights
from decimal import Decimal
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,View,CreateView,FormView,TemplateView



class HomeView(ListView):
    template_name = 'index.html'
    
    def get(self,request):
        products = HomeProduct.objects.filter()
        slides = HomeSlide.objects.all()
        context = {
            'products' : products,
            'slides' : slides,
        }
        return render(request,self.template_name,context)
    
class HomeDetailView(DetailView):
    template_name = 'blog.html'
    
    def get(self,request,id):
        product = HomeProduct.objects.filter.get(pk=id)
        slide = HomeSlide.objects.get(pk=id)
        context = {
            'product' : product,
            'slide' : slide,
        }
        return render(request,self.template_name,context)      
            
def aboutus(request):
    aboutus = 'aboutus.html'
    return render(request,aboutus)

def stays(request):
    neighborhood,city,min_price,max_price,property_status,property_type, BHK,  aminities, bedroom, bathroom = 'stays.html'
    context = {
        'neighborhood': neighborhood,
        'city' : city,
        'min_price' : min_price,
        'max_price' : max_price,
        'property_status' : property_status,
        'property_type' : property_type,
        'BHK' : BHK,
        'aminities' : aminities,
        'bedroom' : bedroom,
        'bathroom' : bathroom
    }
    return render(request,'stays.html',context)

def flights(request):
    flights_from, flights_to = 'flights.html'
    context = {
        'flights_from' : flights_from,
        'flights_to' :flights_to,
    }
    return render(request,'flights.html',context)



