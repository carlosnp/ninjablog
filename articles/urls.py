from django.urls import path

from .views import article_list, article_create, article_detail, article_update, article_delete

app_name = "articles"

urlpatterns = [
    path('', article_list, name="list"),
    path('create/', article_create, name="create"),
    path('<int:id>/', article_detail, name="detail"),
    path('<int:id>/update', article_update, name="update"),
    path('<int:id>/delete', article_delete, name="delete"),
]