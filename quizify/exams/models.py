from datetime import timezone
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from subjects.models import Subject, Topic
from questions.models import Question, Choice
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


class Exam(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    duration = models.PositiveIntegerField()  # Duration in minutes
    maximum_marks = models.PositiveIntegerField()
    has_negative_marking = models.BooleanField(default=False)
    negative_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    num_questions = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class QuestionBlueprint(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_type = models.CharField(
        max_length=100,
        choices=QUESTION_TYPES,
        default='mcq',
    )
    marks = models.PositiveIntegerField()
    difficulty = models.CharField(
        max_length=100,
        choices=QUESTION_DIFFICULTY,
        default='medium',
    )
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"Question for {self.exam.name}"


User = get_user_model()


class UserExam(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    Exam_STATUS = [
        ('active', 'Active'),
        ('started', 'Started'),
        ('finished', 'Finished'),
        ('expired', 'Expired')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.ManyToManyField(
        Question,
        through='UserExamQuestion',
        related_name='user_exams',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    duration = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20, choices=Exam_STATUS, default='active')

    started_at = models.DateTimeField(blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    def finished(self):
        self.status = 'finished'
        self.finished_at = timezone.now()
        self.save()

    class Meta:
        ordering = ['-created_at']


class UserExamQuestion(models.Model):
    user_exam = models.ForeignKey(UserExam, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField(
        default=0)

    def __str__(self):
        return f"{self.user_exam.exam.name} - {self.question}"

    class Meta:
        unique_together = ["user_exam", "question"]


# class Answer(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
#     user_exam = models.ForeignKey(
#         UserExam, on_delete=models.CASCADE, related_name='answers')

#     def __str__(self):
#         return f"{self.user.first_name}'s answer to {self.question.text}"
