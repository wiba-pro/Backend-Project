from rest_framework.views import APIView
from .models import Job
from .permissions import IsJobOwner
from rest_framework import status, generics
from .serializers import jobserializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
# Create your views here.

class Joblist(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        jobs=Job.objects.all()
        serializer=jobserializers(jobs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Job.objects.all()
    serializer_class=jobserializers
    lookup_field="pk"



class EditJob(APIView):
    permission_classes = [IsAuthenticated, IsJobOwner]
    def get_object(self, pk):
        try:
            return Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            return None

    def get(self, request, pk):
        job = self.get_object(pk)
        if job:
            serializer = jobserializers(job)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        job = self.get_object(pk)
        if job and job.user == request.user:
            serializer = jobserializers(job, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk):
        job = self.get_object(pk)
        if job and job.user == request.user:
            job.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)
