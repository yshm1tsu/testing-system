# Generated by Django 3.0.8 on 2020-07-20 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0009_auto_20200720_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='passed_quantity',
            field=models.IntegerField(default=0, verbose_name='Количество прошедших'),
        ),
    ]