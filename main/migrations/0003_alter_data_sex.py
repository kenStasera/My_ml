# Generated by Django 4.2.6 on 2023-10-19 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_alter_data_sex"),
    ]

    operations = [
        migrations.AlterField(
            model_name="data",
            name="sex",
            field=models.PositiveIntegerField(
                choices=[(0, "Female"), (1, "Male")], null=True
            ),
        ),
    ]