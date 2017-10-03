# -*- coding:utf-8 -*-

from django.conf.urls import url

from .views import Home, ViewBikeByCategory, ContactCreateView, ContactUs, WhereWeAre

urlpatterns = [
    url(r'^$',Home.as_view(), name='home'),
    url(r'^motos/categoria/(?P<pk>\d+)/$', ViewBikeByCategory.as_view(), name='views_category'),
    url(r'^contacto/(?P<pk>\d+)/$', ContactCreateView.as_view(), name='contact'),
    url(r'^contactanos/$', ContactUs.as_view(), name='contactus'),
    url(r'^donde_estamos/$', WhereWeAre.as_view(), name='whereWeAre'),
]

