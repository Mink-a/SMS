# Generated by Django 4.1.2 on 2022-10-13 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_gpa'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['id']},
        ),
    ]