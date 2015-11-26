# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ingresar/$', views.ingresar, name='ingresar'),
    url(r'^salir/$', views.salir, name='salir'),
    url(r'^registro/$', views.RegistroCreate.as_view(), name='registro'),
    url(r'^listado-pagina/$', views.listado_paginas, name='listado_paginas'),
    url(r'^crear-pagina/$', views.crear_pagina, name='crear_pagina'),
    url(r'^eliminar-pagina/(?P<pk>\d+)/$', views.eliminar_pagina, name='eliminar_pagina'),
    url(r'^ver-pagina/(?P<pk>\d+)/$', views.ver_pagina, name='ver_pagina'),
]
