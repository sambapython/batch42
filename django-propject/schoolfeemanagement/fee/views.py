# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from forms import SchoolForm, UserForm, OwnUserForm, LoginForm, PaymentHistoryForm
from django.contrib import auth
from django.contrib.auth import authenticate
from models import PaymentHistory, OwnUser
from django.db.models import Sum
def login(f):
	def inner(request):
		user = request.session.get("user")
		if user:
			return f(request)
		else:
			return redirect("/index/")
	return inner


# Create your views here.
def index(request):
	return render(request, "index.html",{'data':"data"})

def get_payment(user):
	data=[]
	if user.role1 == "school":
		ownusers = OwnUser.objects.filter(school=user.school)
		ownuser_ids = map(lambda x:x.id, ownusers)
		data = PaymentHistory.objects.filter(student__id__in=ownuser_ids)
	else:
		data = PaymentHistory.objects.filter(student=user)
	result=[]
	for row in data:
		section_fee = OwnUser.objects.get(id=row.student.id).section.fee
		paid_fee = PaymentHistory.objects.filter(student__id=row.student.id).aggregate(Sum("amount")).get("amount__sum")
		result.append({
			"name":row.student.name,
            "amount":row.amount,
            "school":row.student.school.name,
            "section":row.section.name,
            'date':"%s" % row.date,
            "phone":row.student.phone,
            "due": section_fee-paid_fee,
			})
	return result


def schoolmanagement(request):
	user = request.session.get("user")
	if user:
		ownuser = OwnUser.objects.get(user__username=user)
		data = get_payment(ownuser)
		return render(request, "schoolmanagement.html",{"data":data,
				"school":ownuser.school.name})
	else:
		return redirect("/index/")

def addpayment(request):
	messages = []
	user = request.session['user']
	if user:
		ownuser = OwnUser.objects.get(user__username=user)
		try:
			if request.method=="POST":
				post_data = request.POST
				section_fee = OwnUser.objects.get(id=post_data.get('student')).section.fee
				paid_fee = PaymentHistory.objects.filter(student__id=post_data.get('student')).aggregate(Sum("amount")).get("amount__sum")
			 	if paid_fee:
			 		paying = paid_fee+int(post_data.get("amount"))
			 	else:
			 		paying=int(post_data.get("amount"))
				if section_fee<paying:
					#messages.append("Paying more than the due amount")
					raise Exception("Paying more than the due amount")
				payment = PaymentHistoryForm(request.POST)
				payment.save()
				payment.instance.section = payment.instance.student.section
				payment.save()
				messages.append("payment added successfully to %s"%payment.instance.student.name)
				user = request.session['user']
				ownuser = OwnUser.objects.get(user__username=user)
				data = get_payment(ownuser)
				return redirect("/schoolmanagement/", data)
		except Exception as err:
				messages.append(err.message)
		return render(request, "addpayment.html",{"form":PaymentHistoryForm,
			"messages":messages,"school":ownuser.school.name})
	else:
		return render("login")
	
def create_school(request):
	messages = []
	try:
		if request.method=="POST":
			school = SchoolForm(request.POST)
			school.save()
			messages.append("School created successfully")
	except Exception as err:
			messages.append(err.message)
	return render(request, "create_school.html",{"form":SchoolForm,
		"messages":messages})

def logout(request):
	request.session['user']=None
	return redirect("/index/")

def login(request):
	messages = []
	try:
		if request.method=="POST":
			user = LoginForm(request.POST)
			user = authenticate(username=request.POST['username'],password=request.POST['password'])
			if user:
				ownuser = OwnUser.objects.get(user=user)
				request.session['user']=ownuser.name
				messages.append("Login successfully")
				data = get_payment(ownuser)
				#import pdb; pdb.set_trace()
				if ownuser.role1=="student":
					return render(request,"paymenthistory.html",{"data":data})
				else:

					return redirect("/schoolmanagement/")
			else:
				messages.append("Login failed")
	except Exception as err:
			messages.append(err.message)
	return render(request, "login.html",{"form":LoginForm,
		"messages":messages})

def signup(request):
	messages = []
	try:
		if request.method=="POST":
			user_data = {}
			user_data.update({"username":request.POST.get("username"),
				"password": make_password(request.POST.get("password")),
				"email":request.POST.get("email"),
				 "is_staff":True,
				})
			user =   User(**user_data)
			ouform = OwnUserForm(data = request.POST)
			user.save()
			profile = ouform.save(commit = False)
			profile.user = user
			profile.save()
			messages.append("User created successfully")
	except Exception as err:
			messages.append(err.message)
	return render(request, "signup.html",{"uform":UserForm, "ouform":OwnUserForm,
		"messages":messages})
	
