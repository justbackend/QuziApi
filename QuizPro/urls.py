from django.contrib import admin
from django.urls import path
from app1.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_token/', TokenObtainPairView.as_view()),
    path('refresh_token/', TokenRefreshView.as_view()),
    path('quizzes/', QuizApi.as_view()),
    path('quiz/<int:pk>/', QuizStartApi.as_view()),
    path("quiz_add/", QuizAdd.as_view()),
    path('get_user_id/', CurrentUser.as_view()),
    path('post_answers/', CheckQuiz.as_view()),
    path('register/', UserRegisterApi.as_view()),
]
