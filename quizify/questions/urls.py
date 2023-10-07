from django.contrib import admin
from django.urls import path, include
from questions.views import QuestionListCreateView

urlpatterns = [
    path('', QuestionListCreateView.as_view(),
         name='question-list-create'),
]
