# Generated by Django 3.0.8 on 2020-07-20 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0008_delete_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='passed_quantiry',
            new_name='passed_quantity',
        ),
    ]