# Generated by Django 4.2.3 on 2023-07-28 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_rename_titel_expense_title_rename_titel_income_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='abrserver',
            old_name='titel',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='server',
            old_name='titel',
            new_name='title',
        ),
    ]
