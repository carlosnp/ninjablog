
# Django
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404

def homepage(request):
	template_name = 'homepage.html'
	context = {
	}
	return render(request, template_name, context)
	# return HttpResponse(" <br> <p>Home PAGE</p>")

def about(request):
	template_name = 'about.html'
	context = {
	}
	return render(request, template_name, context)
	# return HttpResponse(" <br> <p>ABOUT</p>")