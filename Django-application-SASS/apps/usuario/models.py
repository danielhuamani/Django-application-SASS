# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from pbkdf2 import crypt
from tenant_schemas.models import TenantMixin


SALT = settings.APLICACION_SASS
NUMERO_DE_ITERACIONES = 500


# Create your models here. #
class Usuario(TenantMixin):
    last_login = models.DateTimeField('Último Login', blank=True, null=True)
    usuario = models.CharField("usuario", max_length=120, unique=True)
    email = models.EmailField(max_length=60, unique=True, db_index=True, blank=True)
    password = models.CharField(max_length=64, verbose_name='Contraseña')
    estado = models.BooleanField("Estado", default=True)
    password_ok = models.BooleanField(u'¿Contraseña encriptada?', default=False)
    auto_create_schema = True

    class Meta:
        ordering = ['usuario']

    def __unicode__(self):
        return self.usuario

    def is_authenticated(self):
        return True

    def is_password_valid(self, password):
        return is_password_valid(password, self.password)

    def save(self, *args, **kwargs):
        if not self.password_ok:
            self.password = encrypt_password(self.password)
            self.password_ok = True

        super(Usuario, self).save(*args, **kwargs)

    @property
    def is_staff(self):
        return False


def encrypt_password(password):
    ''' Encripta la contraseña '''
    return crypt(password, SALT, NUMERO_DE_ITERACIONES)


def is_password_valid(password, encoded):
    ''' Contrasta la contraseña brindada con el valor encriptado '''
    return encrypt_password(password) == encoded
