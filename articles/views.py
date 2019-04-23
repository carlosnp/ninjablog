# Django
from django.shortcuts import render, redirect, get_object_or_404

def article_list(request):
	template_name = 'article_list.html'
	context = {
	}
	return render(request, template_name, context)