# Generated by Django 4.1.3 on 2022-11-10 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Quiz",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.CharField(blank=True, max_length=1000, null=True)),
                ("answer", models.CharField(blank=True, max_length=1000, null=True)),
                ("file", models.FileField(blank=True, null=True, upload_to="files/")),
            ],
        ),
    ]
