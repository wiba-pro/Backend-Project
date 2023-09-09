from django.urls import path, include
from .views import Joblist, JobDetail, EditJob, Createjob, JobSearchView, createjobtype, createcategory, createindustry, createskill

# from rest_framework.authtoken.views import ObtainAuthToken, obtain_auth_token


urlpatterns = [
  
    path('jobs/', Joblist.as_view(), name='jobs'),
    path('job/job/add/', Joblist.as_view(), name='jobs'),
    path('job/<int:pk>/', JobDetail.as_view(), name='job'),
    path('editjob/<int:pk>/', EditJob.as_view(), name='editjob'),
    path('createjob/', Createjob.as_view(), name='createjob'),
    path('jobsearch/', JobSearchView.as_view(), name='jobsearchview'),
    path('jobtype/', createjobtype.as_view(), name='jobtype'),
    path('category/', createcategory.as_view(), name='category'),
    path('industry/', createindustry.as_view(), name='insudtry'),
    path('skill/', createskill.as_view(), name='skill'),
]