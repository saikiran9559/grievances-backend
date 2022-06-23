from dataclasses import fields
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User

from users.models import Profile, StaffProfile

class ProfileSearializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user_role',)

    def save(self, **kwargs):
        return super().save(**kwargs)

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSearializer()
    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name', 'password', 'email', 'date_joined', 'profile']
        extra_kwargs = {'password': {'write_only': True},}

    def create(self, validated_data):
        profile_data = validated_data.pop("profile")
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        Profile.objects.create(user=user, **profile_data)
        print(profile_data)
        return user

class StaffProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffProfile
        fields = '__all__'


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        profile_obj = Profile.objects.get(user__id=self.user.id)
        user_obj = User.objects.get(id=self.user.id)
        data.update({'user': {
            'username': user_obj.username,
            'user_role': profile_obj.user_role
            }
        })
        if(profile_obj.user_role == 2):
            StaffProfile.objects.create(user=self.user)
        return data