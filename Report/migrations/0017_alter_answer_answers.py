# Generated by Django 4.2.20 on 2025-05-08 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Report', '0016_remove_answer_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answers',
            field=models.TextField(help_text='تمامی پاسخ\u200cها در یک فیلد به صورت جداگانه وارد میشوند.', verbose_name='پاسخ\u200cها'),
        ),
    ]
