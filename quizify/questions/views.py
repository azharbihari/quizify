from questions.models import Question, Choice
from questions.serializers import QuestionSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class QuestionListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
