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