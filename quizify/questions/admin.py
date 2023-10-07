from django.contrib import admin
from questions.models import Question, Choice
from django import forms


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'topic', 'difficulty', 'type',
                    'duration', 'created_at', 'updated_at')
    inlines = [ChoiceInline]


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct',
                    'created_at', 'updated_at')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
