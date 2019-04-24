# Django
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Registro de usuario
def signupView(request):
	template_name = 'signup.html'
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		# Si el formulario es valido
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("home")
	else:
		form = UserCreationForm()

	context = {
		"form": form,
	}
	return render(request, template_name, context)

# Inicio de Sesion
def loginView(request):
	template_name = 'login.html'
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect("articles:list")
	else:
		form = AuthenticationForm()
	context = {
		"form": form,
	}
	return render(request, template_name, context)

# Cerrar Sesion
def logoutView(request):
	logout(request)
	return redirect("home")