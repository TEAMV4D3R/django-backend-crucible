from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Job
from .permissions import IsOwnerOrReadOnly
from .serializers import JobSerializer


class ThingList(ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class ThingDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Job.objects.all()
    serializer_class = JobSerializer
