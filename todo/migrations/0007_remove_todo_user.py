# Generated by Django 5.0.7 on 2024-07-23 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0006_todo_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="todo",
            name="user",
        ),
    ]