from django.urls import path
from solutions.views import QuizSolutionListView

urlpatterns = [
    path('<slug:slug>/', QuizSolutionListView.as_view(), name='solution-list'),
]
