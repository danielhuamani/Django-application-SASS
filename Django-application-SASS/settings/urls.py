from django.conf import settings

from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    # Examples:

    url(r'', include('apps.noticia.urls', namespace='noticia')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_URL) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
