from django.urls import path

from .views import ViewORCreateQuestionsAPIView, UpdateQuestionAPIView

urlpatterns = [
    path("", ViewORCreateQuestionsAPIView.as_view()),
    path("updatequestion/<int:pk>/", UpdateQuestionAPIView.as_view()),
]
