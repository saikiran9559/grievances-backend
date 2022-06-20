from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import permissions

from .serializers import ComplaintSerializer
from .models import Complaint


class AllComplaints(ListAPIView):
    serializer_class = ComplaintSerializer
    queryset = Complaint.objects.all()
    permissions=[permissions.IsAuthenticated]


class CreateComplaint(CreateAPIView):
    serializer_class = ComplaintSerializer