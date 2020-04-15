from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

def signup(request):
	if request.method== "POST":
		username= request.POST["username"]
		password= request.POST["password"]
		email= request.POST["email"]

		user = User.objects.create_user(
			username=username,
			password=password,
			email= email
			)
		login(request, user)
		return redirect('/allevents/')
	return render(request,"signup.html")

def signin(request):
	if request.method== "POST":
		username= request.POST["username"]
		password= request.POST["password"]

		user= authenticate(request, username=username,
		 password= password)
		if user != None:
			login(request, user)
			return redirect('/allevents/')

	return render(request,"signin.html")

def signout(request):
	
	logout(request)

	return redirect("/signin/")	
