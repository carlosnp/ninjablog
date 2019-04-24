# Django
from django import forms
# Project
from .models import Article

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ["title", "body", "Image"]