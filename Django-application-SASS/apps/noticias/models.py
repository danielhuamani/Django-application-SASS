from django.db import models


class Noticia(models.Model):
    titulo = models.CharField("Titulo", max_length=120)
    fecha = models.DateTimeField("Fecha", auto_now_add=True)
    contenido = models.TextField("Texto")

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def __str__(self):
        pass
    