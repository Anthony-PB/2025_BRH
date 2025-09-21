from django.urls import path
from . import views

urlpatterns = [
    path("sources/", views.SourceView.as_view(), name="source-create-list"),
    path("sources/get/<str:guid>", views.LoadFromSource.as_view(), name="get-from-source"),
]