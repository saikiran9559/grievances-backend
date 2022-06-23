from rest_framework import serializers
from .models import Complaint, Feedback

class ComplaintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Complaint
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Feedback
        fields = '__all__'