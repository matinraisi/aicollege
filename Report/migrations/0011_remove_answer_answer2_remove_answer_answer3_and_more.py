# Generated by Django 4.2.20 on 2025-05-07 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Report', '0010_listeninganswer_course_readingsubmission_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answer2',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='answer3',
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer1',
            field=models.CharField(default='', max_length=255, verbose_name='پاسخ به سؤال '),
        ),
    ]
