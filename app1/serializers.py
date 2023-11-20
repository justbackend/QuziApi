from .models import *
from rest_framework import serializers
from .models import Quiz, Question, Answer


class QuizSerializer(serializers.Serializer):

    class Meta:
        model = Quiz
        fields = "__all__"

class AnswerGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'answer']


class QuestionGetSerializer(serializers.ModelSerializer):
    answer = AnswerGetSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'question', 'answer']


class QuizGetSerializer(serializers.ModelSerializer):
    question = QuestionGetSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ['id', 'user', 'title', 'date_created', 'duration', 'question']


# ////////////////////////////////////////////////////////////////////

class AnswerPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['answer', 'is_correct']


class QuestionPostSerializer(serializers.ModelSerializer):
    answers = AnswerPostSerializer(many=True)

    class Meta:
        model = Question
        fields = ['question', 'answer']


class QuizPostSerializer(serializers.ModelSerializer):
    questions = QuestionPostSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ['user', 'title', 'duration', 'questions']

    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        quiz = Quiz.objects.create(**validated_data)
        for question_data in questions_data:
            answers_data = question_data.pop('answers')
            question = Question.objects.create(quiz=quiz, **question_data)
            for answer_data in answers_data:
                Answer.objects.create(question=question, **answer_data)
        return quiz




class QuizCheckSerializer(serializers.Serializer):
    quiz = serializers.IntegerField()
    duration = serializers.CharField(max_length=10)
    answers = serializers.ListField(child=serializers.IntegerField())


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "_all__"



class UserRegisterSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(required=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'age']



