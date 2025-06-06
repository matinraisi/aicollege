# Generated by Django 4.2.20 on 2025-05-07 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0035_remove_question_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='question_images/', verbose_name='تصویر')),
            ],
        ),
        migrations.CreateModel(
            name='PdfFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='question_pdfs/', verbose_name='فایل PDF')),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='question1',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='سؤال '),
        ),
        migrations.AddField(
            model_name='question',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='questions', to='courses.image', verbose_name='تصاویر'),
        ),
        migrations.AddField(
            model_name='question',
            name='pdf_files',
            field=models.ManyToManyField(blank=True, related_name='questions', to='courses.pdffile', verbose_name='فایل\u200cهای PDF'),
        ),
    ]
