from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
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
        fields = ['id','username', 'first_name', 'last_name', 'password', 'email', 'date_joined', 'profile']
        extra_kwargs = {'password': {'write_only': True},}

    def create(self, validated_data):
        profile_data = validated_data.pop("profile")
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        Profile.objects.create(user=user, **profile_data)
        return user




class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        profile_obj = Profile.objects.get(user__id=self.user.id)
        user_obj = User.objects.get(id=self.user.id)
        data.update({'user': {
            'username': user_obj.username,
            'is_staff': profile_obj.is_staff, 
            'is_student': profile_obj.is_student, 
            'is_admin': profile_obj.is_admin
            }
        })
        return data