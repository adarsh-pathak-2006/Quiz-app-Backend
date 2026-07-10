from rest_framework.serializers import ModelSerializer
from core.models import Quiz, QuestionSet, Result
from django.contrib.auth import get_user_model

User=get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email', 'role']

class RegisterSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email', 'role', 'password']

class QuizSerializer(ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Quiz
        fields='__all__'

class QuestionSeializer(ModelSerializer):
    quiz=QuizSerializer(read_only=True)
    class Meta:
        model=QuestionSet
        fields='__all__'

class ResultSerializer(ModelSerializer):
    student=UserSerializer(read_only=True)
    quiz=QuizSerializer(read_only=True)
    class Meta:
        model=Result
        fields='__all__'

class AIRequestSerializer(ModelSerializer):
    class Meta:
        model=Quiz
        fields=['topic', 'difficulty', 'no_of_ques']

class AIResponseSerializer(ModelSerializer):
    class Meta:
        model=QuestionSet
        fields=['question', 'option1', 'option2', 'option3', 'option4', 'correct_answer']

