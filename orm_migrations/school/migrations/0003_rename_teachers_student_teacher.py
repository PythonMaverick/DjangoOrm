# Generated by Django 4.1.2 on 2022-10-26 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0002_remove_student_teacher_student_teachers_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student", old_name="teachers", new_name="teacher",
        ),
    ]