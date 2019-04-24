# Django
from django.shortcuts import render, redirect

# Registro de usuario
def signupView(request):
	template_name = 'signup.html'
	context = {
	}
	return render(request, template_name, context)
