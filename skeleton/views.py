from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Skeleton_form
from .models import Skeleton
from django.contrib import messages
from django.contrib.auth.models import User, auth #auth for login
# Create your views here.

## very basic page
# def home_view(request, *args, **kwargs):
# 	return HttpResponse("My home page")

##working with templates 
# def home_view(request):
# 	return render(request, "home.html") 	


def home_view(request):
	return render(request, "home.html")

##basic create view page
#def create_view(request):
#	return render(request, "create.html")

def create_view(request):
	form = Skeleton_form(request.POST or None)
	if form.is_valid():
		form.save()
		form=Skeleton_form()
	context = {
		'form': form
	}
	return render(request, "create.html", context)

##basic read view
#def read_view(request):
#	return render(request, "read.html")

def read_view(request):
	o=Skeleton.objects.all()
	context={
		'obj':o
	}
	return render(request, "read.html", context)

# def update_view(request):
# 	return render(request, "update.html")

def list_update_view(request):
	o=Skeleton.objects.all()
	context = {
	'obj': o
	}
	return render(request, "list_update.html", context)

def update_view(request, ids):
	o=Skeleton.objects.get(id=ids)
	form = Skeleton_form(request.POST or None, instance=o)
	if form.is_valid():
		form.save()
		form=Skeleton_form()
	context = {
		'form': form
	}
	return render(request, "create.html", context)

# def delete_view(request):
#  	return render(request, "delete.html")

def list_delete_view(request):
	o=Skeleton.objects.all()
	context = {
	'obj': o
	}
	return render(request, "list_delete.html", context)

def delete_view(request, ids):
	o=Skeleton.objects.get(id=ids)
	if request.method=='POST':
		o.delete()
		return redirect("http://127.0.0.1:8000/")

	context={
	'obj': o
	}
	return render(request, "delete.html", context)


def register_view(request):

	if request.method=="POST":
		firstname=request.POST['f_n']
		lastname=request.POST['l_n']
		user_name=request.POST['u_n']
		password1=request.POST['p_1']
		password2=request.POST['p_2']
		email_address=request.POST['e_a']

		if password1==password2:
			if User.objects.filter(username=user_name).exists():
				print("username already exists")
			elif User.objects.filter(email=email_address).exists():
				print("Email already exists")
			else:
				user=User.objects.create_user(first_name=firstname, last_name=lastname, username=user_name, password=password1, email=email_address)
				user.save()
				print("User created")
				return render(request,"login.html")
		else:
			print("Password mismatch")
			return render(request, "user_registration.html")

	else:
		return render(request, "user_registration.html")

def login_view(request):
	if request.method=='POST':
		user_name=request.POST['u_n']
		password=request.POST['p']
		user=auth.authenticate(username=user_name, password=password)

		if user is not None:
			auth.login(request, user)
			messages.info(request, "User logged in successfully!")
			print("User logged in")
			return redirect("http://127.0.0.1:8000/")
		else:
			messages.info(request, "Invalid credentials")
			print("Invalid credentials")
			return render(request, "login.html")

	else:
		return render(request, "login.html")