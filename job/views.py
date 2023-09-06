from rest_framework.views import APIView
from .models import Job
from .permissions import IsJobOwner
from rest_framework import status, generics
from .serializers import jobserializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
# Create your views here.

class Joblist(APIView):
    permission_classes=[AllowAny]
    def get(self, request):
        jobs=Job.objects.all()
        serializer=jobserializers(jobs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Job.objects.all()
    serializer_class=jobserializers
    lookup_field="pk"

class Createjob(generics.CreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Job.objects.all()
    serializer_class = jobserializers


class EditJob(APIView):
    permission_classes = [IsAuthenticated, IsJobOwner, AllowAny]
    def get_object(self, pk):
        try:
            return Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            return None

    def post(self, request, pk):
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

class JobSearchView(APIView):
    permission_classes=[AllowAny]
    def get(self, request):
        jobtype = request.query_params.get('jobtype')
        industry = request.query_params.get('industry')
        category = request.query_params.get('category')
        skill = request.query_params.get('skill')

        Jobs = Job.objects.all()

        if jobtype:
            Jobs = Jobs.filter(jobtype__title= jobtype)

        if industry:
            Jobs = Job.filter(industry__title=industry)
        
        if category:
            Jobs = Job.filter(category__title=category)
        
        if skill:
            Jobs = Job.filter(skill__title=industry)
            
        serializer = jobserializers(Jobs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # def post(self, request):
    #     jobs=jobtype.objects.all()
    #     serializer=jobserializers(jobs, many=True)