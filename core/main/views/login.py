# from django.shortcuts import render, redirect, HttpResponseRedirect
# from django.contrib.auth.hashers import check_password
# from main.models.customer import Customer
# from django.views import View
# from django.contrib.auth.forms import AuthenticationForm
# from main.forms import NewUserForm, AddCart
# from django.contrib.auth import login, authenticate,logout
# from django.contrib import messages

# def login_request(request):
#     if request.method == "POST":
# 	    form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 		 	password = form.cleaned_data.get('password')
# 		 	user = authenticate(username=username, password=password)
# 		    if user is not None:
# 			login(request, user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return redirect("index")
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request=request, template_name="login.html", context={"login_form":form})

# def logout_request(request):
# 	logout(request)
# 	messages.info(request, "You have successfully logged out.") 
# 	return redirect("home")
