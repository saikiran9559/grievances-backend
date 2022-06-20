from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import ComplaintSerializer
from .models import Complaint


class AllComplaints(ListAPIView):
    serializer_class = ComplaintSerializer
    queryset = Complaint.objects.all()


class CreateComplaint(CreateAPIView):
    serializer_class = ComplaintSerializer