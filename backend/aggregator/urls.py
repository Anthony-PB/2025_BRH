from django.urls import path
from .views import SourceView, LoadFromSource

urlpatterns = [
    path("sources/", SourceView.as_view(), name="source-create-list"),
    path("sources/get/<str:guid>", LoadFromSource.as_view(), name="get-from-source"),
]
