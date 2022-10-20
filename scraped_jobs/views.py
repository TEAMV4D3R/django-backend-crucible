from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Active_job
from .serializers import ActiveJobSerializer

class ActiveJobList(ListCreateAPIView):
    queryset = Active_job.objects.all()
    serializer_class = ActiveJobSerializer

class ActiveJobDetail(RetrieveUpdateDestroyAPIView):
    queryset = Active_job.objects.all()
    serializer_class = ActiveJobSerializer
