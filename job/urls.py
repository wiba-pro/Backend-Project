from django.urls import path, include
from .views import Joblist, JobDetail, EditJob

# from rest_framework.authtoken.views import ObtainAuthToken, obtain_auth_token


urlpatterns = [
    path('jobs/', Joblist.as_view(), name='jobs'),
    path('job/<int:pk>/', JobDetail.as_view(), name='job'),
    path('editjob/<int:pk>/', EditJob.as_view(), name='editjob'),
    
]