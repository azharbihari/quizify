from rest_framework import generics
from quizzes.models import Quiz
from solutions.serializers import QuizSolutionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class QuizSolutionListView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSolutionSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        user = self.request.user
        if user.has_active_subscription:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response({"detail": "You don't have an active subscription to access this quiz's solutions."}, status=status.HTTP_403_FORBIDDEN)
