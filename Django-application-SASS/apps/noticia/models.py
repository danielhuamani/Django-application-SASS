from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
ESTADO = (
  ('P', 'PUBLICADO'),
  ('R', 'REVISADO'),
  )


class Noticia(models.Model):
    titulo = models.CharField("Titulo", max_length=120)
    estado = models.CharField("Estado", max_length=120, choices=ESTADO, default='P')
    fecha = models.DateField('Fecha', auto_now=True)
    imagen = models.ImageField('imagen', max_length=100, upload_to="imagen")
    contenido = models.TextField("Contenido")

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def get_delete_url(self):
        return reverse('usuario:eliminar_pagina', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse('usuario:ver_pagina', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.titulo
