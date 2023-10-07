from django.contrib import admin
from django.urls import path, include
from subjects.views import SubjectListCreateView

urlpatterns = [
    path('', SubjectListCreateView.as_view(),
         name='subject-list-create'),
]
