from django.urls import path
from .views import CreateUser, UsersList, CustomTokenObtainPairView, home

urlpatterns = [
    path('', home, name='home'),
    path('login', CustomTokenObtainPairView.as_view(), name='login'),
    path('users', UsersList.as_view(), name='users'),
    path('register', CreateUser.as_view(), name='register-user')
]
