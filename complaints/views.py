from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import permissions

from .serializers import ComplaintSerializer, FeedbackSerializer
from .models import Complaint, Feedback


class AllComplaints(ListAPIView):
    serializer_class = ComplaintSerializer
    queryset = Complaint.objects.all()
    permissions=[permissions.IsAuthenticated]

    def get_queryset(self):
        query_set = self.queryset.filter(user=self.request.user)
        return query_set

class CreateComplaint(CreateAPIView):
    serializer_class = ComplaintSerializer
    permissions=[permissions.IsAuthenticated]


class AllFeedbacks(ListAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permissions=[permissions.IsAuthenticated]

    def get_queryset(self):
        query_set = self.queryset.filter(given_to=self.request.user)
        return query_set
 
class CreateFeedback(CreateAPIView):
    serializer_class = FeedbackSerializer
    permissions = [permissions.IsAuthenticated]

