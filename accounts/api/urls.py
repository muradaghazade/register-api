from django.urls import path
from .views import RegisterUserAPI, ShowUsersAPI

app_name = 'register_api'

urlpatterns = [
    path('register/', RegisterUserAPI.as_view(), name='register'),
    path('show-users/', ShowUsersAPI.as_view(), name='user-list'),
]