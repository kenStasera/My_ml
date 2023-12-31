# Generated by Django 4.2.6 on 2023-10-19 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Data",
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
                ("name", models.CharField(max_length=100, null=True)),
                ("age", models.PositiveIntegerField(null=True)),
                ("height", models.PositiveIntegerField(null=True)),
                (
                    "sex",
                    models.CharField(
                        choices=[(0, "Female"), (1, "Male")], max_length=20, null=True
                    ),
                ),
                (
                    "predictions",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-date"],
            },
        ),
    ]
