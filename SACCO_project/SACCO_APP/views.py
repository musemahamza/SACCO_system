import email
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login

# Create your views here.
def Login(request):
  msg=None
  form=Loginform(request.POST or None)
  if request.method== "POST":
    if form.is_valid():
      username=form.cleaned_data.get ("username")
      password=form.cleaned_data.get ("password")
      user=authenticate(username=username,password=password)
      if user is not None:
        login(request,user )
        return redirect('home')
      else: 
        msg= "Invalid username or password"
    else: 
      msg = "Error while validating form"

  return render(request,"Login.html",{"form":form, "msg": msg})

def index(request):
	msg=None
	if request.method == "POST":
		form=coursesform(request.POST)
		if form.is_valid():
			user=form.save()
			msg="Class Created successfully"
			return redirect('home')
		else:
			msg="Form is not valid" 
	else:
		form=coursesform()
	return render(request,'index.html',{'form':form, 'msg':msg})


def home(request):
	msg=None
	return render(request,'home.html',{'msg':msg})


def classes(request):
	Sacco = loans.objects.all()
	msg=None
	return render(request,'classes.html',{'msg':msg,'LoanDetails':Sacco})


def updateview(request, id):
  mymember = loans.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def updaterecordview(request, id):
  firstname = request.POST['firstname']
  middlename = request.POST['middlename']
  lastname = request.POST['lastname']
  contact_no = request.POST['contact_no']
  address = request.POST['address']
  email = request.POST['email']
  g_name = request.POST['g_name']
  phone_number = request.POST['phone_number']
  g_address = request.POST['g_address']

  member = loans.objects.get(id=id)
  member.firstname = firstname
  member.middlename = middlename
  member.lastname = lastname
  member.contact_no = contact_no
  member.address= address
  member.email = email
  member.g_name = g_name
  member.phone_number = phone_number
  member.g_address = g_address
  member.save()
  return HttpResponseRedirect(reverse('home'))



def deleteview(request, id):
  member = loans.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('classes'))