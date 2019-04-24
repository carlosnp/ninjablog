# Django
from django.contrib import admin

# Project
from .models import Article

class ArticleModelAdmin(admin.ModelAdmin):
	list_display = ('title', 'data', 'updated')
	search_fields = ["title", "body"]

admin.site.register(Article, ArticleModelAdmin)