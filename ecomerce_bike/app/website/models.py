# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        default_permissions = ()
        permissions = (
            ('ver_categorias','Puede ver las categorias'),
            ('editar_categorias','Puede editar las categorias'),
            ('borrar_categorias','Puede borrar las categorias'),
        )

    def __unicode__(self):
        return u'{0}'.format(self.name)

    def __str__(self):
        return self.name

class Bike(models.Model):
    name = models.CharField(max_length=256, verbose_name='Nombre')
    motor = models.CharField(max_length=256, verbose_name='Motor')
    cylinder = models.CharField(max_length=266, verbose_name='Cilindraje')
    photo = models.ImageField(upload_to='media/', default = 'media/None/no-img.png')
    category = models.ForeignKey(Category)

    class Meta:
        verbose_name = 'Moto'
        verbose_name_plural = 'Motos'
        default_permissions = ()
        permissions = (
            ('ver_moto', 'Puede ver las Motos'),
            ('editar_moto', 'Puede editar las motos'),
            ('borrar_moto', 'Puede borrar las motos'),
        )

    def __unicode__(self):
        return u'{0}'.format(self.name)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=256, verbose_name='Nombre')
    email = models.EmailField(verbose_name='Correo')
    subjet = models.TextField(verbose_name='Asunto')
    bike = models.ForeignKey(Bike)

    class Meta:
        verbose_name = 'contacto'
        verbose_name_plural = 'contactanos'
        default_permissions = ()
        permissions = (
            ('ver_contacto', 'Puede ver los contactos'),
            ('editar_moto', 'Puede editar los contactos'),
            ('borrar_moto', 'Puede borrar los contactos'),
        )

    def __unicode__(self):
        return u'{0}'.format(self.name)

    def __str__(self):
        return self.name
