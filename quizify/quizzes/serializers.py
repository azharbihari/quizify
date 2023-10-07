from django.utils import timezone
from datetime import timedelta
from rest_framework import serializers
from quizzes.models import Quiz, Answer, Result
from questions.serializers import QuestionSerializer
from accounts.serializers import UserSerializer
from subjects.serializers import SubjectSerializer, TopicSerializer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuizDetailSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    topic = TopicSerializer(read_only=True)
    number_of_questions = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = ['id', 'name', 'user', 'slug', 'subject',
                  'topic', 'duration', 'number_of_questions', 'difficulty']

    def get_number_of_questions(self, obj):
        return obj.questions.count()


class ResultSerializer(serializers.ModelSerializer):
    # Use the simplified serializer
    quiz = QuizDetailSerializer(read_only=True)

    class Meta:
        model = Result
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    answers = AnswerSerializer(many=True, read_only=True)
    subject = SubjectSerializer(read_only=True)
    remaining_time = serializers.SerializerMethodField()
    topic = TopicSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    result = ResultSerializer(read_only=True)

    class Meta:
        model = Quiz
        fields = '__all__'

    def get_remaining_time(self, instance):
        if instance.started_at:
            remaining_time = (
                instance.started_at + timedelta(seconds=instance.duration)) - timezone.now()
            return max(remaining_time.total_seconds(), 0)
        return 0

    def update(self, instance, validated_data):
        instance.started_at = timezone.now()
        instance.status = 'started'
        instance.save()
        return instance
