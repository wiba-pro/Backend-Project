from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status, generics
from .serializers import userserializers



from rest_framework.permissions import AllowAny
# Create your views here.

class Userlist(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=userserializers

