# Generated by Django 4.0.1 on 2022-01-08 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='file_name',
            field=models.ImageField(upload_to='app/static/uploads/'),
        ),
    ]
