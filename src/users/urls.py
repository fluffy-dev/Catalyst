from django.urls import path
from users.apis import UserCreateApi

urlpatterns = [
    path('register/', UserCreateApi.as_view(), name='register'),
]