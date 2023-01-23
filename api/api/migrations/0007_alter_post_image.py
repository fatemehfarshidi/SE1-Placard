# Generated by Django 4.1.5 on 2023-01-21 19:00

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='media/nopicture.png', null=True, upload_to=api.models.upload_to, verbose_name='Image'),
        ),
    ]