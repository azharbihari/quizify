from django.utils import timezone
from django.db import models
from subjects.models import Subject, Topic
from questions.models import Question, Choice
import uuid
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class Quiz(models.Model):
    QUIZ_STATUS = [
        ('active', 'Active'),
        ('started', 'Started'),
        ('finished', 'Finished'),
        ('expired', 'Expired')
    ]

    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    difficulty = models.CharField(
        max_length=10, choices=Question.QUESTION_DIFFICULTY, default='medium')
    questions = models.ManyToManyField(Question)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    duration = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20, choices=QUIZ_STATUS, default='active')

    started_at = models.DateTimeField(blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.name = f"{self.subject.name} - {self.topic.name} Quiz"
            self.slug = str(uuid.uuid4()).replace('-', '')[:16]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def finished(self):
        self.status = 'finished'
        self.finished_at = timezone.now()
        self.save()

    class Meta:
        ordering = ['-created_at']


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return f"{self.user.first_name}'s answer to {self.question.text}"


class Result(models.Model):
    quiz = models.OneToOneField(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()

    def __str__(self):
        return f"Result for {self.user.first_name } in {self.quiz.name}"
