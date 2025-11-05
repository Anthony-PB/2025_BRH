from django.urls import path
from .views import (
    SourceView,
    SourceDetailView,
    ArticleListView,
    ArticleDetailView,
    BookmarkArticleView,
    LoadFromSource,
)

urlpatterns = [
    path("sources/", SourceView.as_view(), name="source-list-create"),
    path("sources/<int:pk>/", SourceDetailView.as_view(), name="source-detail"),
    path("sources/<int:source_id>/load/", LoadFromSource.as_view(), name="load-from-source"),
    path("articles/", ArticleListView.as_view(), name="article-list"),
    path("articles/<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
    path("articles/<int:article_id>/bookmark/", BookmarkArticleView.as_view(), name="bookmark-article"),
]
