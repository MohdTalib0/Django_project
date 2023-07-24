from django.urls import path
from .views import QualificationListCreateView, QualificationRetrieveUpdateDeleteView

urlpatterns = [
    path('qualifications/', QualificationListCreateView.as_view(), name='qualification-list-create'),
    path('qualifications/<int:pk>/', QualificationRetrieveUpdateDeleteView.as_view(), name='qualification-retrieve-update-delete'),
]
