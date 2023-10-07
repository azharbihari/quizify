from django.db import models
from questions.models import Question


class Solution(models.Model):
    question = models.OneToOneField(
        Question, on_delete=models.CASCADE, related_name='solution')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Solution for {self.question.text}"
