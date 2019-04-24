# Django
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Registro de usuario
def signupView(request):
	template_name = 'signup.html'
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		# Si el formulario es valido
		if form.is_valid():
			form.save()
			return redirect("home")
	else:
		form = UserCreationForm()
	
	context = {
		"form": form,
	}
	return render(request, template_name, context)
