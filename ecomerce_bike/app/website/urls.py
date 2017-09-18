# -*- coding:utf-8 -*-

from django.conf.urls import url

from .views import Home, ViewBikeByCategory, ContactCreateView

urlpatterns = [
    url(r'^$',Home.as_view(), name='home'),
    url(r'^motos/categoria/(?P<pk>\d+)/$', ViewBikeByCategory.as_view(), name='views_category'),
    url(r'^contacto/(?P<pk>\d+)/$', ContactCreateView.as_view(), name='contact'),
]

