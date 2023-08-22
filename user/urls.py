from django.urls import path, include
from . import views
# from rest_framework.authtoken.views import ObtainAuthToken, obtain_auth_token


urlpatterns = [
    path('users/', views.Userlist.as_view(), name='users'),    
]