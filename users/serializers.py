from rest_framework import serializers
from django.contrib.auth.models import User

from users.models import Profile

class ProfileSearializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('is_admin', 'is_staff', 'is_student')

    def save(self, **kwargs):
        return super().save(**kwargs)

    

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSearializer()
    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name', 'email', 'date_joined', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop("profile")
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user


