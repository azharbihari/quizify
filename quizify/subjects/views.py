from subjects.models import Subject
from subjects.serializers import SubjectSerializer
from rest_framework import generics


class SubjectListCreateView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
