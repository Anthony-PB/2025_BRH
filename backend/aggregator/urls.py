from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="aggregator-index"),
    # Add more URLs as you build features:
    # path("articles/", views.article_list, name="article-list"),
    # path("sources/", views.source_list, name="source-list"),
]