#coding: utf8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify


@python_2_unicode_compatible
class Categoria(models.Model):
	nombre = models.CharField(max_length=25)

	def __str__(self):
		return self.nombre
@python_2_unicode_compatible
class Articulo(models.Model):
	titulo =models.CharField(max_length=35)
	slug = models.SlugField(unique=True, null=True, blank=True)
	portada = models.ImageField(upload_to='portadas',default = "portada01.png", blank=True,null=True)
	autor =	models.ForeignKey(User)
	categoria=models.ForeignKey(Categoria, blank=False,null=False)
	fecha = models.DateTimeField(auto_now_add=True)
	contenido = models.TextField()
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(default=0)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.titulo)
		super(Articulo,self).save(*args, **kwargs)

		
	def __str__(self):
		return self.titulo + ':' + self.slug

@python_2_unicode_compatible
class Comentario(models.Model):
	fecha = models.DateTimeField(auto_now_add=True)
	contenido = models.TextField()
	articulo =models.ForeignKey(Articulo)

	def __str__(self):
		return self.contenido
	