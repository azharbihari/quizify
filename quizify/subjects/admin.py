from django.contrib import admin
from subjects.models import Subject, Topic
from django import forms


class TopicInline(admin.TabularInline):
    model = Topic
    extra = 1


class SubjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}
    list_display = ('name', 'created_at', 'updated_at')
    inlines = [TopicInline]


class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}
    list_display = ('name', 'subject', 'created_at', 'updated_at')


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Topic, TopicAdmin)
