from django.urls import path
from src.users.apis import UserCreateApi

urlpatterns = [
    path('register/', UserCreateApi.as_view(), name='register'),
]