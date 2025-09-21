from django.urls import path
from . import views

urlpatterns = [
    path('sources/', views.SourceView.as_view(), name='source-create'),
    # Add more endpoints as needed:
    # path("articles/", views.ArticleView.as_view(), name="article-list"),
]
