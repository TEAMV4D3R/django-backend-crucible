from rest_framework import serializers
from .models import Active_job


class ActiveJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Active_job
        fields = "__all__"
