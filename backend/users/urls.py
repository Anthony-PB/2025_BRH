from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('profile/', views.UserView.as_view(), name='user-profile'),
    path('follow/<str:source_id>/',
         views.FollowSourceView.as_view(), name='follow-source'),
    path('unfollow/<str:source_id>/',
         views.UnfollowSourceView.as_view(), name='unfollow-source'),
    path('login/', views.LoginUserView.as_view(), name='login'),
]
