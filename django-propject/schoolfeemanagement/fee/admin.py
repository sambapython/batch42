# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from  models import School, Section, OwnUser

# Register your models here.
for i in [School, Section, OwnUser]:
	admin.site.register(i)
