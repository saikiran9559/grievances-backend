from rest_framework import serializers
from .models import Complaint, Feedback

class ComplaintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Complaint
        fields = ['id', 'user', 'subject', 'body', 'viewed', 'created']
        extra_kwargs = {'user': {'required': False}}
    
    def create(self, validated_data):
        complaint = Complaint(**validated_data, user=self.context['request'].user)
        complaint.save()
        return complaint

class FeedbackSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Feedback
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}

    def create(self, validated_data):
        feedback = Feedback(**validated_data, user=self.context['request'].user)
        feedback.save()
        return feedback