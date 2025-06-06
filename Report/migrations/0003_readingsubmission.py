# Generated by Django 4.2.20 on 2025-05-06 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0024_delete_readingsubmission'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Report', '0002_listeninganswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadingSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_file', models.FileField(upload_to='reading_audios/', verbose_name='فایل صوتی ضبط\u200cشده')),
                ('submitted_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.readingexercise', verbose_name='تمرین')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'پاسخ تمرین روخوانی',
                'verbose_name_plural': 'ارسال\u200cهای تمرین روخوانی',
                'ordering': ['-submitted_at'],
            },
        ),
    ]
