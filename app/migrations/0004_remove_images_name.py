# Generated by Django 4.0.1 on 2022-01-09 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_file_name_images_file_images_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='name',
        ),
    ]
