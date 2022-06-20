from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    is_checked = models.BooleanField(default=False)
    viewed = models.BooleanField(default=False)


    def __str__(self):
        return self.subject