from django.urls import path
from .views import UserList, home

urlpatterns = [
    path('', home, name='home'),
    path('users', UserList.as_view(), name='users')
]
