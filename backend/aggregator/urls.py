from django.urls import path
from .views import SourceView

urlpatterns = [
    path('sources/', SourceView.as_view(), name='source-create'),
]
