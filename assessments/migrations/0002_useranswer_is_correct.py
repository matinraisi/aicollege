# Generated by Django 5.1.7 on 2025-03-15 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswer',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]
