from django.urls import path
from .views import RegisterUserView, FollowSourceView, UnfollowSourceView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('follow/<str:source_id>/',
         FollowSourceView.as_view(), name='follow-source'),
    path('unfollow/<str:source_id>/',
         UnfollowSourceView.as_view(), name='unfollow-source'),
]
