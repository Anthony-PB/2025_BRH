from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register-user'),
    path('profile/', views.UserView.as_view(), name='profile-manager'),
    # Add other endpoints as needed
]