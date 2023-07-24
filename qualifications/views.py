from rest_framework import generics
from .models import Qualification
from .serializers import QualificationSerializer

class QualificationListCreateView(generics.ListCreateAPIView):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer

class QualificationRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer
