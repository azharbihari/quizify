from django.contrib import admin
from exams.models import QuestionBlueprint, Exam, UserExam


class QuestionBlueprintInline(admin.TabularInline):
    model = QuestionBlueprint


class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'created_at', 'updated_at')
    inlines = [QuestionBlueprintInline]


admin.site.register(Exam, ExamAdmin)
admin.site.register(UserExam)
