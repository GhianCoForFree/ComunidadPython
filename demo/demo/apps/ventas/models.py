from django.db import models

class Cliente(models.Model):
	nombre = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)
	estado = models.BooleanField(default=True)

	def __unicode__(self):
		nombrecompleto = '%s %s' % (self.nombre,self.apellidos)
		return nombrecompleto

class Producto(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.TextField(max_length=300)
	precio = models.IntegerField()
	estado = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre
