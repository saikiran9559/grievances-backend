from django.urls import path
from .views import AllComplaints, CreateComplaint


urlpatterns = [
    path('complaints', AllComplaints.as_view(), name='complaints'),
    path('complaints/add', CreateComplaint.as_view(), name='create-complaint')
]
