from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Winner
from .permissions import IsOwnerOrReadOnly
from .serializers import WinnerSerializer


class ThingList(ListCreateAPIView):
    queryset = Winner.objects.all()
    serializer_class = WinnerSerializer


class ThingDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Winner.objects.all()
    serializer_class = WinnerSerializer
