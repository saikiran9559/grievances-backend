from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User

from users.serializers import UserSerializer, CustomTokenObtainPairSerializer

@api_view(['GET'])
def home(request):
    return Response({'data': 'hello world'})

class UsersList(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class CreateUser(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes= []
    authentication_classes=[]

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer