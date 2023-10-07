from exams.models import Subject, Topic, Quiz, Choice, Answer, Result
from questions.models import Question
from exams.serializers import QuizSerializer, ResultSerializer, QuizDetailSerializer
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
import random
from rest_framework import generics
from django.contrib.auth.models import User


class QuizView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    lookup_field = 'slug'


class QuizDetailView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizDetailSerializer
    lookup_field = 'slug'


class QuizListCreateView(generics.ListCreateAPIView):
    serializer_class = QuizSerializer

    def get_queryset(self):
        # Return only quizzes associated with the current user
        return Quiz.objects.filter(user=self.request.user)


class QuizRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    lookup_field = 'slug'


class SaveAnswer(views.APIView):
    def post(self, request, slug):
        try:
            quiz = Quiz.objects.get(slug=slug)
        except Quiz.DoesNotExist:
            return Response({'error': 'Quiz not found'}, status=status.HTTP_404_NOT_FOUND)

        user = request.user
        question = Question.objects.get(pk=request.data.get('question'))
        choice = Choice.objects.get(pk=request.data.get('choice'))

        if question and choice:
            answer, created = Answer.objects.get_or_create(
                user=user, question=question, defaults={'choice': choice}, quiz=quiz)

            if not created:
                answer.choice = choice
                answer.save()

            answer.save()

            return Response({'message': 'Answer saved successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Invalid question or choice'}, status=status.HTTP_400_BAD_REQUEST)


class GenerateQuizView(views.APIView):
    def post(self, request):
        # Extract user preferences from the request data
        user = request.user
        subject = Subject.objects.filter(
            pk=request.data.get('subject')).first()
        topic = Topic.objects.filter(pk=request.data.get('topic')).first()
        difficulty = request.data.get('difficulty')

        # Query questions based on user preferences
        questions = Question.objects.filter(
            subject=subject,
            topic=topic,
            difficulty=difficulty
        )

        num_questions = 5
        selected_questions = random.sample(list(questions), num_questions)
        duration = sum([question.duration for question in selected_questions])

        quiz = Quiz.objects.create(
            user=user,
            subject=subject,
            topic=topic,
            difficulty=difficulty,
            duration=duration
        )

        quiz.questions.set(selected_questions)

        serializer = QuizSerializer(quiz)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class QuizFinishView(views.APIView):
    def post(self, request, slug):
        try:
            user = request.user
            quiz = Quiz.objects.get(slug=slug)
        except Quiz.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        score = 0
        for answer in quiz.answers.all():
            if answer.choice.is_correct:
                score += 1

        # Update quiz status and create a result
        quiz.finished()
        result = Result.objects.create(
            quiz=quiz, user=user, score=score)

        return Response(status=status.HTTP_200_OK)


class QuizResultView(views.APIView):
    def get(self, request, slug):
        try:
            quiz = Quiz.objects.get(slug=slug)
            result = Result.objects.get(quiz=quiz)

            serializer = ResultSerializer(result)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Quiz.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
