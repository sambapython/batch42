# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import Customer

# Create your views here.
def fun(request):
	#return HttpResponse("hell world")
	#return HttpResponse("<h1>hell world</h1>")
	data = Customer.objects.all()
	if request.method=="POST":
		name=request.POST.get("cust_name")
		email=request.POST.get("cust_email")
		cust_obj=Customer(name=name, email=email)
		cust_obj.save()
		data = Customer.objects.all()
	return render(request, "index.html",{"data":data})
