from rest_framework import serializers
from .models import Complaint, Feedback


class ComplaintSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Complaint
        fields = ['id', 'user', 'subject', 'body', 'viewed', 'created', 'user_name']
        extra_kwargs = {'user': {'required': False}}
    
    def create(self, validated_data):
        complaint = Complaint(**validated_data, user=self.context['request'].user)
        complaint.save()
        return complaint

    def get_user_name(self, obj):
        return str(obj.user.username)


class FeedbackSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Feedback
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}

    def create(self, validated_data):
        feedback = Feedback(**validated_data, user=self.context['request'].user)
        feedback.save()
        return feedback

    def get_user_name(self, obj):
        return str(obj.user.username)