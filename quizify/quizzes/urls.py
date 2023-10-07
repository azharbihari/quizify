from django.contrib import admin
from django.urls import path, include
from quizzes.views import QuizListCreateView, QuizDetailView, SaveAnswer, GenerateQuizView, QuizFinishView, QuizResultView, QuizRetrieveUpdateView

urlpatterns = [
    path('', QuizListCreateView.as_view(),
         name='quiz-list-create'),

    path('create/', GenerateQuizView.as_view(), name='quiz-create'),
    path('<slug:slug>/', QuizDetailView.as_view(), name='quiz-detail'),
    path('<slug:slug>/start/', QuizRetrieveUpdateView.as_view(), name='quiz-start'),
    path('<slug:slug>/finish/', QuizFinishView.as_view(), name='quiz-finish'),
    path('<slug:slug>/result/', QuizResultView.as_view(), name='quiz-result'),
    path('<slug:slug>/answer/',
         SaveAnswer.as_view(), name='quiz-answer'),
]
