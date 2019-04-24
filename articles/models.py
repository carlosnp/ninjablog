from django.db import models

# Create your models here.
class Article(models.Model):
	title 	= models.CharField("Titulo",max_length=100)
	slug 	= models.SlugField()
	body	= models.TextField("Contenido")
	data 	= models.DateTimeField("Fecha de creación", auto_now_add=True)
	# thumbnail
	# Author

	def __str__(self):
		return str(self.title)