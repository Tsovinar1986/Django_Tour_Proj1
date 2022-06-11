from asyncio.log import logger
from multiprocessing import context
from django.dispatch import receiver
from django.shortcuts import render, redirect
from .models import  HomeProduct, HomeSlide,aboutus,stays,flights,Cart,UserCarts
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from decimal import Decimal
from django.urls import reverse
from django.http import HttpResponse
from .forms import NewUserForm, AddCart
from django.views.generic import ListView,DetailView,View,CreateView,FormView,TemplateView


def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, 'Registration is successfull')
            return redirect('index')
        messages.error(request,'Unsuccessfull registration. Invalid Information.')
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")

class HomeListView(ListView):
    template_name = 'index.html'
    
    def get(self,request):
        prods = HomeProduct.objects.filter()
        slides = HomeSlide.objects.all()
        return render(request,self.template_name,{'prods':prods, 'slides' :slides})
   
class  Homedetail(DetailView):
    template_name = 'blog.html'
    
    def get(self,request,id):
        prod = HomeProduct.objects.get(pk=id)
        slide = HomeSlide.objects.get(pk=id)
        return render(request,self.template_name,{'prod':prod,'slide':slide})


def flights(request):
    flights  = 'flights.html'
    return render(request, 'flights.html', {'flights':flights})

def stays(request):
    stays = 'stays.html'
    return render(request, 'stays.html', {'stays':stays})

    
# def add_post(request):
#     	form = AddCart()
# 	    if request.method == 'POST':
# 			form = AddCart(request.POST)
# 		    if form.is_valid():
# 			   form.save()
# 			   context = {'form':form}
# 			   return redirect('post_detail')
# 		    else:
# 			    form = AddCart()
# 			    context = {'form':form}
# 	    else:
# 		         form = AddCart()
# 		context = {'form':form}
# 	return render(request, 'add_post.html', context)
	            
# def post_detail(request):
# 	carts = UserCarts.objects.all()
# 	return render(request, 'post_detail.html', {'carts':carts})


# class UserPageListView(ListView):
#     template_name = 'userpage.html'

#     def get(self, request):
#         users = NewUserForm(request.POST)
		
#         return render(request, self.template_name, {'users':users, 'form':form})


