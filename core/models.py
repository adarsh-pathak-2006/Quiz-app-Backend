from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    STUDENT='STUDENT'
    TEACHER='TEACHER'

    ROLE_CHOICES=[(STUDENT, 'Student'), (TEACHER, 'Teacher')]

    role=models.CharField(max_length=7, choices=ROLE_CHOICES)


class Quiz(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    topic=models.CharField(max_length=100)
    difficulty=models.models.CharField(choices=[('EASY', 'Easy'), ('MEDIUM', 'Medium'), ('HARD', 'Hard')] , max_length=6)
    no_of_ques=models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.user.first_name
    
class QuestionSet(models.Model):
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questionset')
    question=models.TextField(null=True)
    option1=models.TextField(null=True)
    option2=models.TextField(null=True)
    option3=models.TextField(null=True)
    option4=models.TextField(null=True)
    correct_answer=models.CharField(choices=[('A', option1), ('B', option2), ('C', option3), ('D', option4)])

    def __str__(self):
        return self.question[:80]
    
class Result(models.Model):
    student=models.ForeignKey(User, on_delete=models.CASCADE)
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE)
    obtained_mark=models.PositiveIntegerField()
    total_marks=models.PositiveIntegerField()

    def __str__(self):
        return self.student.first_name
