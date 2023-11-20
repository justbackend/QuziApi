from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    score = models.PositiveBigIntegerField(default=0)
    age = models.PositiveIntegerField()


class Category(models.Model):
    category = models.CharField(max_length=100)


class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="quiz")
    title = models.CharField(max_length=150)
    date_created = models.DateField(auto_now_add=True)
    duration = models.PositiveIntegerField()


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='question')
    question = models.TextField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    answer = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="result")
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    correct = models.PositiveIntegerField()
    duration = models.CharField(max_length=10)
