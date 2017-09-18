# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.contrib import admin

# Register your models here.
class BikeAdmin(admin.ModelAdmin):
    list_display = ('name', 'motor', 'description', 'cylinder', 'photo','category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subjet', 'bike')

admin.site.register(Bike, BikeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Contact, ContactAdmin)