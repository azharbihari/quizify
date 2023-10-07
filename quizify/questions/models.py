from django.db import models
from django.utils.text import slugify
from subjects.models import Subject, Topic


class Question(models.Model):

    QUESTION_DIFFICULTY = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )

    QUESTION_TYPES = [
        ('text', 'Text'),
        ('mcq', 'Multiple Choice'),
        ('msq', 'Multiple Select'),
        ('numerical', 'Numerical'),
    ]

    text = models.TextField()
    type = models.CharField(
        max_length=20, choices=QUESTION_TYPES, default='mcq')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    difficulty = models.CharField(
        max_length=10, choices=QUESTION_DIFFICULTY, default='medium')
    duration = models.PositiveIntegerField(default=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


class Choice(models.Model):
    text = models.CharField(max_length=200)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='choices')
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
