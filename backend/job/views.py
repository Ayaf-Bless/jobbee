from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Job
from .serializers import JobSerializer


# Create your views here.


@api_view(["GET"])
def getAllJobs(request):
    """end point to get all the jobs"""
    job = Job.objects.all()

    serializer = JobSerializer(job, many=True)
    return Response(serializer.data)
