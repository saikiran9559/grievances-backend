from django.urls import path
from .views import AllComplaints, CreateComplaint, AllFeedbacks, CreateFeedback


urlpatterns = [
    path('complaints', AllComplaints.as_view(), name='complaints'),
    path('complaints/add', CreateComplaint.as_view(), name='create-complaint'),
    path('feedback/all', AllFeedbacks.as_view(), name='feedbacks'),
    path('feedback/add', CreateFeedback.as_view(), name='create-feedback')
]
