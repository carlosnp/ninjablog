# Django
from django.urls import path
# Project
from .views import signupView, loginView, logoutView 

app_name = "accounts"

urlpatterns = [
	# Registro de usuario
    path('signup/', signupView, name="signup"),
    path('login', loginView, name="login"),
    path('logout/', logoutView, name="logout"),
]