from django.urls import path
from .views import RegisterUserView, FollowSourceView, UnfollowSourceView
from .views import RegisterUserView, FollowSourceView, UnfollowSourceView

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('profile/', views.UserView.as_view(), name='user-profile'),
    path('follow/<str:source_id>/',
         FollowSourceView.as_view(), name='follow-source'),
    path('unfollow/<str:source_id>/',
         UnfollowSourceView.as_view(), name='unfollow-source'),
]
