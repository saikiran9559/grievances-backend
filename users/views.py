from requests import request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, CreateAPIView

from users.serializers import UserSerializer

@api_view(['GET'])
def home(request):
    return Response({'data': 'hello world'})

class UsersList(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class CreateUser(CreateAPIView):
    serializer_class = UserSerializer
