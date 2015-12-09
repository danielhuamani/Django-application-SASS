# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext as ctx
from django.views.generic import CreateView
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils import timezone
from django.contrib import messages
from .models import Usuario
from .forms import IngresarForm


def ingresar(request):
    ''' Vista de login '''
    usuario_principal = get_object_or_404(Usuario, schema_name='public')
    print (usuario_principal.domain_url)
    if request.method == "POST":
        dominio = request.POST.get("dominio")+"."+usuario_principal.domain_url

        usuario = get_object_or_404(Usuario, domain_url=dominio)

        print (dominio+".localhost:8004")
        return HttpResponseRedirect("http://"+dominio+":8000")
    return render_to_response('portal/login.html', locals(), context_instance=ctx(request))


def salir(request):
    logout(request)
    return redirect(reverse('usuario:ingresar'))


class RegistroCreate(CreateView):
    ''' Vista para registrar usuario, se uso vistas basadas en clases '''
    model = Usuario
    fields = ['usuario', 'password', 'email', 'schema_name', 'domain_url']
    template_name = 'portal/registro.html'
    success_url = reverse_lazy('usuario:ingresar')
