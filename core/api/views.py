from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializers import UserRegistrationSerializer

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