# Generated by Django 3.2.3 on 2021-05-18 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vjc', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='titile',
            new_name='title',
        ),
    ]