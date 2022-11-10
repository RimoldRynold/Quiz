from django.http import FileResponse, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from quiz.models import Quiz

from .serializers import QuizSerializer


class ViewORCreateQuestionsAPIView(APIView):
    def get(self, request):
        articles = Quiz.objects.all()
        serializer = QuizSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuizSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateQuestionAPIView(APIView):
    def get_object(self, pk):
        try:
            return Quiz.objects.get(id=pk)
        except Quiz.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = QuizSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            file_handle = article.file.open()
            response = FileResponse(file_handle, content_type="application/pdf")
            response["Content-Length"] = article.file.size
            response["Content-Disposition"] = (
                'attachment; filename="%s"' % article.file.name
            )
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
