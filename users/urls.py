from django.urls import path
from .views import CreateUser, UsersList, home

urlpatterns = [
    path('', home, name='home'),
    path('users', UsersList.as_view(), name='users'),
    path('register', CreateUser.as_view(), name='register-user')
]
