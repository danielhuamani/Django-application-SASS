# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^ingresar/$', views.ingresar, name='ingresar'),
    url(r'^salir/$', views.salir, name='salir'),
    url(r'^$', views.RegistroCreate.as_view(), name='registro'),

]
