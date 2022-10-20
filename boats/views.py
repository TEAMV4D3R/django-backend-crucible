from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Boat
from .permissions import IsOwnerOrReadOnly
from .serializers import BoatSerializer


class ThingList(ListCreateAPIView):
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer


class ThingDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer
