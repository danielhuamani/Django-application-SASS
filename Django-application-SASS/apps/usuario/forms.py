# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate
from .models import Usuario
from django import forms
from apps.noticia.models import Noticia


class IngresarForm(forms.Form):
    usuario = forms.CharField(label='usuario')
    password = forms.CharField(label='Contraseña')

    def clean_usuario(self):
        usuario = self.cleaned_data['usuario']
        try:
            Usuario.objects.get(usuario=usuario)
        except Usuario.DoesNotExist:
            mensaje = "El usuario no ha sido registado"
            raise forms.ValidationError(mensaje)
        return usuario

    def auth(self):
        cd = self.cleaned_data
        print cd['usuario']
        print cd['password']
        return authenticate(username=cd['usuario'], password=cd['password'])


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['estado', 'imagen', 'contenido', 'titulo']
