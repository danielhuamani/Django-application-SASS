# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext as ctx
from django.views.generic import CreateView
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils import timezone
from django.contrib import messages
from .models import Usuario
from .forms import IngresarForm, NoticiaForm
from apps.noticia.models import Noticia


def ingresar(request):
    ''' Vista de login '''
    if request.method == "POST":
        form = IngresarForm(request.POST)

        if form.is_valid():
            user = form.auth()
            if user is not None:
                if user.estado:
                    user.last_login = timezone.now()
                    user.save()
                    login(request, user)
                    return redirect(reverse('usuario:listado_paginas'))
                else:
                    messages.add_message(request, messages.WARNING, 'Usuario no se encuentra registrado')
            else:
                messages.add_message(request, messages.WARNING, u'El email y contraseña son inválidos')
    else:
        form = IngresarForm()

    return render_to_response('portal/login.html', locals(), context_instance=ctx(request))


def salir(request):
    logout(request)
    return redirect(reverse('usuario:ingresar'))


class RegistroCreate(CreateView):
    ''' Vista para registrar usuario, se uso vistas basadas en clases '''
    model = Usuario
    fields = ['usuario', 'password', 'email']
    template_name = 'portal/registro.html'
    success_url = reverse_lazy('usuario:ingresar')


@login_required(login_url=reverse_lazy('usuario:ingresar'))
def listado_paginas(request):
    ''' Vista para mostrar la tabla de las entradas creadas'''
    noticias = Noticia.objects.all().order_by('-fecha')
    return render_to_response('portal/listado-pagina.html', locals(), context_instance=ctx(request))


@login_required(login_url=reverse_lazy('usuario:ingresar'))
def crear_pagina(request):
    ''' Vista para crear un entradas'''
    if request.method == "POST":
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('usuario:listado_paginas'))
    else:
        form = NoticiaForm()
    return render_to_response('portal/crear-pagina.html', locals(), context_instance=ctx(request))


def ver_pagina(request, pk):
    ''' Vista ver el detalle de una pagina'''
    noticia = get_object_or_404(Noticia, pk=pk)
    return render_to_response('portal/ver-pagina.html', locals(), context_instance=ctx(request))


@login_required(login_url=reverse_lazy('usuario:ingresar'))
def eliminar_pagina(request, pk):
    ''' Vista que sirver para eliminar luego hacer una redireccion'''
    noticia = get_object_or_404(Noticia, pk=pk)
    noticia.delete()
    return redirect(reverse_lazy('usuario:listado_paginas'))
