# Generated by Django 4.2.20 on 2025-05-07 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0031_question_season'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserCourse',
        ),
    ]
