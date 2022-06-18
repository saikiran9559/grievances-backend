from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User

from users.serializers import UserSerializer

@api_view(['GET'])
def home(request):
    return Response({'data': 'hello world'})


class UserList(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()