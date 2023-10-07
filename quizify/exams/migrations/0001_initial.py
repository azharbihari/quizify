# Generated by Django 4.2.4 on 2023-09-10 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0001_initial'),
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('duration', models.PositiveIntegerField()),
                ('maximum_marks', models.PositiveIntegerField()),
                ('has_negative_marking', models.BooleanField(default=False)),
                ('negative_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('num_questions', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='UserExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('duration', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('active', 'Active'), ('started', 'Started'), ('finished', 'Finished'), ('expired', 'Expired')], default='active', max_length=20)),
                ('started_at', models.DateTimeField(blank=True, null=True)),
                ('finished_at', models.DateTimeField(blank=True, null=True)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.exam')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='UserExamQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.PositiveIntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.question')),
                ('user_exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.userexam')),
            ],
            options={
                'unique_together': {('user_exam', 'question')},
            },
        ),
        migrations.AddField(
            model_name='userexam',
            name='questions',
            field=models.ManyToManyField(related_name='user_exams', through='exams.UserExamQuestion', to='questions.question'),
        ),
        migrations.AddField(
            model_name='userexam',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='QuestionBlueprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(choices=[('text', 'Text'), ('mcq', 'Multiple Choice'), ('msq', 'Multiple Select'), ('numerical', 'Numerical')], default='mcq', max_length=100)),
                ('marks', models.PositiveIntegerField()),
                ('difficulty', models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], default='medium', max_length=100)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.exam')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.subject')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.topic')),
            ],
        ),
    ]