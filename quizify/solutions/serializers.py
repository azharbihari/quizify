from rest_framework import serializers
from solutions.models import Solution
from questions.models import Question
from quizzes.models import Quiz
from accounts.serializers import UserSerializer


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = '__all__'


class QuestionSolutionSerializer(serializers.ModelSerializer):
    solution = SolutionSerializer(read_only=True)

    class Meta:
        model = Question
        fields = '__all__'


class QuizSolutionSerializer(serializers.ModelSerializer):
    questions = QuestionSolutionSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Quiz
        fields = '__all__'
