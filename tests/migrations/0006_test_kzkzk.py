# Generated by Django 3.0.8 on 2020-07-20 08:53

from django.db import migrations, models
import tests.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0005_question_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='kzkzk',
            field=models.CharField(default=tests.helpers.random_code, max_length=5, verbose_name='Код'),
        ),
    ]
