# Generated by Django 4.1.5 on 2023-01-09 04:47

import api.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('type', models.CharField(choices=[('Borrow', 'Borrow'), ('Sell', 'Sell'), ('Collab', 'Collab')], default='Sell', max_length=20)),
                ('price', models.FloatField(null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('contact_type', models.CharField(choices=[('Phone number', 'Phone number'), ('Telegram', 'Telegram'), ('Email', 'Email'), ('Other', 'Other')], default='Phone number', max_length=20)),
                ('contact_info', models.CharField(max_length=250)),
                ('image', models.ImageField(default='posts/default.jpg', null=True, upload_to=api.models.upload_to, verbose_name='Image')),
                ('slug', models.SlugField(blank=True, max_length=250, unique=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
    ]
