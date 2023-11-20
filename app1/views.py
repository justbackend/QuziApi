from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db import transaction

class QuizApi(APIView):
    def get(self, request):
        model = Quiz.objects.all()
        serializer = QuizSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class QuizStartApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        model = Quiz.objects.filter(id=pk)
        serializer = QuizGetSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class QuizAdd(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = QuizPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "Saved successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CurrentUser(APIView):
    def get(self, request):
        user_id = request.user.id
        return Response({"user_id": user_id})


class CheckQuiz(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = QuizCheckSerializer(data=request.data)
        if serializer.is_valid():
            count = 0
            length = 0
            answers = serializer.validated_data.get('answers')
            quiz_id = serializer.validated_data.get('quiz')
            quiz = Quiz.objects.get(id=quiz_id)
            duration = serializer.validated_data.get('duration')
            for answer in answers:
                correct = Answer.objects.get(id=answer).is_correct
                length += 1
                if correct:
                    count += 1

            result = Result.objects.create(
                user=request.user,
                quiz=quiz,
                correct=count,
                duration=duration
            )
            # user = User.objects.get(user=request.user)
            # # togri_javob_foiz*duration*savol_soni*level
            # user.score+=quiz.duration/result.duration * count/length*length

            return Response("amazing")


class UserRegisterApi(APIView):
    @transaction.atomic
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            age = serializer.validated_data.pop("age")
            user = serializer.save()
            Profile.objects.create(user=user, age=age)
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


