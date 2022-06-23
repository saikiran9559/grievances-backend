from operator import mod
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    viewed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    given_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='given_to')
    course = models.CharField(max_length=100)
    q1 = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    q2 = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    q3 = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    q4 = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    q5 = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user.username} to {self.given_to.username}'