from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Task

#user registration serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required = True)
    confirm_password = serializers.CharField(write_only = True, required = True)

    class Meta:
        model = User
        fields = ['username','password','confirm_password','email']
    
    def validate(self, attrs):

        #check if the password match
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"error":"password did not match"})
        return attrs
    
    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


#user change password serializer
class UserChangePasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(write_only = True, required = True)
    confirm_password = serializers.CharField(write_only = True, required = True)

    class Meta:
        model = User
        fields = ['new_password','confirm_password']

    def validate(self, attrs):
        #check if the password is match
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"error":"password did not match"})
        return attrs

    def save(self, **kwargs):
        user = kwargs.get('user')
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user


#user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']


#serializer for task
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title','description','status','created_at','updated_at']