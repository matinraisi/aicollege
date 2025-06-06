# Generated by Django 4.2.20 on 2025-05-05 07:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0014_alter_answer_options_remove_answer_response_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vocabularylesson',
            name='pronunciation_audio',
        ),
        migrations.RemoveField(
            model_name='vocabularylesson',
            name='user',
        ),
        migrations.AlterField(
            model_name='vocabularylesson',
            name='image',
            field=models.ImageField(upload_to='words/', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='vocabularylesson',
            name='translation',
            field=models.CharField(max_length=200, verbose_name='ترجمه فارسی'),
        ),
        migrations.CreateModel(
            name='UserPronunciation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pronunciation_audio', models.FileField(upload_to='pronunciations/', verbose_name='فایل تلفظ')),
                ('is_correct', models.BooleanField(verbose_name='تلفظ صحیح بود؟')),
                ('attempt_number', models.IntegerField(default=1, verbose_name='شماره تلاش')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='زمان ثبت')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.vocabularylesson', verbose_name='لغت')),
            ],
            options={
                'verbose_name': 'تلفظ کاربر',
                'verbose_name_plural': 'تلفظ\u200cهای کاربران',
            },
        ),
    ]
