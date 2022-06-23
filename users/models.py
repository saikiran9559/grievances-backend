from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = [
        (1, 'Admin'),
        (2, 'Staff'),
        (3, 'Student')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)

    def __str__(self):
        return f'{self.user.username} profile'

class StaffProfile(models.Model):
    COURSE_TYPE = [
        (1, 'Theory'),
        (2, 'Lab Subject'),
        (3, 'Lab Staff')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff_profile')
    course = models.CharField(max_length=255)
    course_type = models.PositiveSmallIntegerField(choices=COURSE_TYPE)

    def __str__(self):
        return f'{self.user.username} staff profile'

    
