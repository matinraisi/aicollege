# Generated by Django 4.2.20 on 2025-05-07 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0039_questions_remove_question_questions_and_more'),
        ('Report', '0011_remove_answer_answer2_remove_answer_answer3_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'پاسخ سوالات', 'verbose_name_plural': 'پاسخ\u200c سوالات'},
        ),
        migrations.RemoveField(
            model_name='answer',
            name='answer1',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='answer',
            name='answers',
            field=models.TextField(default='', help_text='تمامی پاسخ\u200cها را در یک فیلد به صورت جداگانه وارد کنید.', verbose_name='پاسخ\u200cها'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='season',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.season', verbose_name='درس مرتبط'),
        ),
    ]
