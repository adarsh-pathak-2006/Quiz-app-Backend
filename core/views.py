from django.shortcuts import render
from core.serializers import RegisterSerializer, UserSerializer, QuizSerializer, QuestionSeializer, ResultSerializer, AIRequestSerializer, AIResponseSerializer
from core.models import Quiz, QuestionSet, Result
from rest_framework.views import APIView


class RegisterAPI(APIView):
    def post(self, request):
        serial=Register




