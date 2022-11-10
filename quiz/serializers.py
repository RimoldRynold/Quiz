import datetime
import os

from django.conf import settings
from django.core.files import File
from rest_framework import serializers

from quiz.generate_pdf import save_pdf

from .models import Quiz


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.answer = validated_data.get("answer", instance.answer)
        timestamp = datetime.datetime.now().microsecond
        pdf_name = "question" + "_" + str(timestamp) + ".pdf"
        filename = settings.PROJECT_PATH + "/temppdf/" + pdf_name
        save_pdf(filename, instance.question, instance.answer)
        file_to_save = open(filename, "rb")
        instance.file.save(pdf_name, File(file_to_save))
        file_to_save.close()
        os.remove(r"%s" % filename)
        instance.save()
        return instance
