#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

#Segun lo que entendi aqui se van agregando las clases a utilizar en el proyecto con sus respectivos atributos,
#los atributos se declaran y de acuerdo al valor asignado se determina el tipo de dato del mismo

#Esta es la clase Bebida
class Bebida(models.Model):
	#este es el atributo nombre, de tipo CharField, con la propiedad max_length
	nombre=models.CharField(max_length=50)
	ingredientes=models.TextField()
	preparacion=models.TextField()

	def __unicode__(self):
		return self.nombre

class Receta(models.Model):
	titulo = models.CharField(max_length=100, verbose_name='Título', unique=True)
	ingredientes = models.TextField(help_text='Redacta los ingredientes')
	preparacion = models.TextField(verbose_name='Preparación', help_text='El proceso de preparación')
	imagen = models.ImageField(upload_to='recetas', verbose_name='Imágen')
	tiempo_registro = models.DateTimeField(auto_now=True)
	usuario = models.ForeignKey(User)	

	def __unicode__(self):
		return self.titulo

class Comentario(models.Model):
	receta = models.ForeignKey(Receta)
	texto = models.TextField(help_text='Tu comentario', verbose_name='Comentario')

	def __unicode__(self):
		return self.texto
				