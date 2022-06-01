from rest_framework import serializers

from .models import Job


class JobSerializer(serializers.ModelSerializer):
    """serializer for job"""

    class Meta:
        model = Job
        fields = "__all__"
