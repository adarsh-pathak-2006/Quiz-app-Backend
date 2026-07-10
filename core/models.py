from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    question=models.TextField(null=True)
    answer=models.TextField(null=True)

    def __str__(self):
        return self.user.first_name

