from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('profile/', views.UserView.as_view(), name='user-profile'),
    path('sources/<uuid:source_id>/follow/',
         views.FollowSourceView.as_view(), name='follow-unfollow-source'),
    path('login/', views.LoginUserView.as_view(), name='login'),
]
