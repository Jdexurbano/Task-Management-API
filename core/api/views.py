from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from core.models import Task
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer, TaskSerializer

class UserRegistrationView(APIView):

    @swagger_auto_schema(request_body = UserRegistrationSerializer)
    def post(self,request):
        serializer = UserRegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response({
            "message":"validation failed",
            "errors":serializer.errors,
        }, status = status.HTTP_400_BAD_REQUEST)


class TaskListView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self,request):
        user = User.objects.get(username = request.user)
        tasks = user.tasks.all()
        serializer = TaskSerializer(tasks,many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)