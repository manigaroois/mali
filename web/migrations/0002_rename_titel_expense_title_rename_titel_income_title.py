# Generated by Django 4.2.3 on 2023-07-28 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='titel',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='income',
            old_name='titel',
            new_name='title',
        ),
    ]
