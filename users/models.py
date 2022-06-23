from statistics import mode
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} profile'

class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff_profile')
    course = models.CharField(max_length=255)
    is_theory = models.BooleanField(default=False)
    is_lab = models.BooleanField(default=False)
    is_lab_staff = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} staff profile'

    
