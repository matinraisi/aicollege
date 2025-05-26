from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class Question(models.Model):
    text = models.TextField()
    level = models.CharField(max_length=50)

class UserAnswer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    audio_response = models.FileField(upload_to='audios/', null=True, blank=True)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)