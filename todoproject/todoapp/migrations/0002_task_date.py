# Generated by Django 4.1.1 on 2022-11-19 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todoapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="date",
            field=models.DateField(default="1992-01-01"),
            preserve_default=False,
        ),
    ]
