# Generated by Django 4.1.5 on 2023-01-31 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='type',
        ),
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('Sell', 'خرید و فروش'), ('StudyBuddy', 'تیم سازی ')], default='Sell', max_length=20),
        ),
    ]