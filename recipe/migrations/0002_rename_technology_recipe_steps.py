# Generated by Django 3.2.7 on 2021-09-23 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='technology',
            new_name='steps',
        ),
    ]
