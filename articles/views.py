# Django
from django.shortcuts import render, redirect
# Project
from .models import Article
from .forms import ArticleForm

# Lista de Articulos
def article_list(request):
	template_name = 'article_list.html'
	articles = Article.objects.all().order_by("date")
	context = {
		'articles': articles,
	}
	return render(request, template_name, context)

# Detalles de un Articulo
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

# Actualizar un Articulo
def article_update(request, id=None):
    template_name = 'article_create.html'
    
    try:
    	instance = Article.objects.get(id=id)
    except:
    	template_names 	= "404.html"
    	detail_comment = "El Artículo que buscas no existe"
    	contextdata = {
    		"detail_comment": detail_comment,
    	}
    	return render(request, template_names, contextdata, status = 404)
    # Formulario
    form = ArticleForm(request.POST or None, instance=instance)
    # Verificamos que el formulario es valido
    if form.is_valid():
    	instance = form.save(commit = False)
    	instance.save()
    	return redirect("articles:detail", id=id)
    # Contexto
    context = {
    	"title":'Actualizar',
    	"articles": instance,
    	"form": form
    }
    return render(request, template_name, context)