# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from .models import Category, Bike, Contact


class Home(TemplateView):
    template_name = "website/home.html"
    model = Category
    second_model = Bike

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        context['categories'] = self.model.objects.all()
        context['last_bikes'] = self.second_model.objects.filter().order_by('-id')[:3]
        return context

class ViewBikeByCategory(ListView):
    model = Bike
    second_model = Category
    template_name = 'website/view_bikes.html'

    def get_object(self):
        return get_object_or_404(self.second_model, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        context['categories'] = self.second_model.objects.all()
        category_id = self.get_object().id
        context['category']= self.get_object().name
        context['bikes'] = self.model.objects.filter(category=category_id)
        return context

class ContactCreateView(CreateView):
    model = Contact
    template_name = 'website/form_contact.html'
    fields = ['name','email','celphone', 'subjet']
    success_url = reverse_lazy('home')

    def get_object(self):
        return get_object_or_404(Bike, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        bike = self.get_object()
        context['bike'] = bike.name
        return context

    def form_valid(self, form):
        form.instance.bike = self.get_object()
        form.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        super(self.__class__, self).form_invalid(form)
        context = {'error': 'Ocurrio un error al guardar', 'form': form}
        print form.errors
        return render(self.request, self.template_name, context)

class ContactUs(TemplateView):
    template_name = 'website/contactUs.html'

class WhereWeAre(TemplateView):
    template_name = 'website/whereweare.html'