# Generated by Django 3.2.9 on 2021-11-20 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stringapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stringdata',
            old_name='name',
            new_name='string_data',
        ),
    ]