from django.db import models

# Create your models here.
class Article(models.Model):
	title 	= models.CharField("Titulo",max_length=100)
	slug 	= models.SlugField()
	body	= models.TextField("Contenido")
	data 	= models.DateTimeField("Fecha de creación", auto_now=False, auto_now_add=True)
	updated = models.DateTimeField("Fecha de Actualización",auto_now=True, auto_now_add=False)
	# thumbnail
	# Author
	class Meta:
		verbose_name = 'Artículo'
		verbose_name_plural = 'Artículos'
	
	def __str__(self):
		return str(self.title)