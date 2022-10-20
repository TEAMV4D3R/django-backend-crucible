from rest_framework import serializers
from .models import Officer


class BoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officer
        fields = "__all__"
