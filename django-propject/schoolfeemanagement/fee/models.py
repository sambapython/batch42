# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class School(models.Model):
	name = models.CharField(max_length=250)
	address = models.TextField()
	def __unicode__(self):
			return self.name

class Section(models.Model):
	name = models.CharField(max_length=250)
	fee = models.IntegerField()
	school = models.ForeignKey(School)
	def __unicode__(self):
			return "%s, %s"%(self.school.name,self.name)

class OwnUser(models.Model):
	user = models.OneToOneField(User)
	types_choices = [('student', "student"), ("school", "school")]
	name = models.CharField(max_length=250)
	phone = models.CharField(max_length=250)
   	#children = models.ManyToManyField(OwnUser, blank=True, null=True)
   	role1 = models.CharField(choices=types_choices, max_length=30)
   	school = models.ForeignKey(School)
   	section = models.ForeignKey(Section, blank=True, null=True)
	def __unicode__(self):
			return "%s, %s"%(self.name,self.school.name)

class PaymentHistory(models.Model):
	amount = models.IntegerField()
	student = models.ForeignKey(OwnUser)
	date = models.DateField(auto_now_add=True)
	section = models.ForeignKey(Section, blank=True, null=True)
	def __unicode__(self):
			return "%s->%s"%(self.student.name, self.amount)