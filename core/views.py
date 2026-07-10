from django.shortcuts import render
from core.serializers import RegisterSerializer, UserSerializer, QuizSerializer, QuestionSeializer, ResultSerializer, AIRequestSerializer, AIResponseSerializer
from core.models import Quiz, QuestionSet, Result
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response


User=get_user_model()

class RegisterAPI(APIView):
    def post(self, request):
        serial=RegisterSerializer(data=request.data)
        if serial.is_valid():
            first_name=serial.validated_data['first_name']
            last_name=serial.validated_data['last_name']
            username=serial.validated_data['username']
            email=serial.validated_data['email']
            password=serial.validated_data['password']
            role=serial.validated_data['role']

            if User.objects.filter(username=username).exists():
                return Response({ 'message':'user already exists' })
            else:
                User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password, role=role)
                return Response({ 'message':'registration Successfull' })
        else:
            return Response({ 'message':'invalid inputs' })



