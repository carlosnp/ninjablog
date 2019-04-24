# Django
from django.shortcuts import render, redirect, get_object_or_404
# Project
from .models import Article

# Lista de Articulos
def article_list(request):
	template_name = 'article_list.html'
	articles = Article.objects.all().order_by("date")
	context = {
		'articles': articles,
	}
	return render(request, template_name, context)

def article_detail(request, id):
	template_name = 'article_detail.html'
	try:
		instance = Article.objects.get(id=id)
	except:
		template_names 	= "404.html"
		detail_comment = "El Artículo que buscas no existe"
		contextdata = {
			"detail_comment": detail_comment,
			}
		return render(request, template_names, contextdata, status = 404)
	context = {
		'article': instance,
	}
	return render(request, template_name, context)