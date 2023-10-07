from django.contrib import admin
from quizzes.models import Quiz, Answer, Result
from django import forms


class QuizAdmin(admin.ModelAdmin):
    list_display = ('user', 'topic', 'difficulty', 'created_at', 'updated_at')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'choice', 'question')


class ResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'score')


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Result, ResultAdmin)
