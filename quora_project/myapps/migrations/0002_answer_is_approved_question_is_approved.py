# Generated by Django 4.1.5 on 2023-07-23 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
