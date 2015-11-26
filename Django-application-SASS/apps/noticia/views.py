# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext as ctx
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Noticia


def home(request):
    noticias = Noticia.objects.all().order_by("-fecha")
    return render_to_response('portal/home.html', locals(), context_instance=ctx(request))
