from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from core.models import Task
from django.contrib.auth.models import User
from rest_framework.exceptions import NotFound
from .serializers import UserRegistrationSerializer, TaskSerializer, UserChangePasswordSerializer, UserSerializer

#user registartion view
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


#USER views
class UserChangePasswordView(APIView):
    
    @swagger_auto_schema(request_body = UserChangePasswordSerializer)
    def patch(self,request):
        serializer = UserChangePasswordSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response({"message":"password change succesfully"},status = status.HTTP_201_CREATED)
        return Response({
            "message":"validation failed",
            "errors":serializer.errors,
        },status = status.HTTP_400_BAD_REQUEST)


class UserEditInfoView(APIView):
    
    @swagger_auto_schema(request_body = UserSerializer, responses = {201:UserSerializer()})
    def patch(self,request):
        user = User.objects.get(username = request.user)
        serializer = UserSerializer(user, data = request.data)
        if serializer.is_valid():
            #pass the user
            serializer.save(user = request.user)
            return Response({"message":"account successfully edit","data":serializer.data},status = status.HTTP_201_CREATED)
        return Response({"error":serializer.errors},status = status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):

    @swagger_auto_schema(responses = {200:UserSerializer()})
    def get(self,request):
        user = User.objects.get(username = request.user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status = status.HTTP_200_OK)



#TASK views
class TaskListView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses = {200:TaskSerializer()})
    def get(self,request):
        user = User.objects.get(username = request.user)
        tasks = user.tasks.all()
        serializer = TaskSerializer(tasks,many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body = TaskSerializer,responses = {201:TaskSerializer()})
    def post(self,request):
        serializer = TaskSerializer(data = request.data)
        if serializer.is_valid():
            #pass the user
            serializer.save(user = request.user)
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response({
            "errors":serializer.errors
        },status = status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self,user,task_id):
        try:
            user = User.objects.get(username = user)
            return user.tasks.get(pk = task_id)
        except Task.DoesNotExist:
            raise NotFound(detail = 'task not found')
    
    @swagger_auto_schema(responses = {200:TaskSerializer()})
    def get(self,request,task_id):
        task = self.get_object(request.user,task_id)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status = status.HTTP_200_OK)
    

    @swagger_auto_schema(request_body = TaskSerializer, responses = {201:TaskSerializer()})
    def put(self,request,task_id):
        task = self.get_object(request.user,task_id)
        serializer = TaskSerializer(task, data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response({
            "message":"update error",
            "errors":serializer.errors
        },status = status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request,task_id):
        task = self.get_object(request.user,task_id)
        task.delete()
        return Response({"message":"task deleted successfully"},status = status.HTTP_204_NO_CONTENT)
