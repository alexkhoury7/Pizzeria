# Generated by Django 3.0.5 on 2022-12-11 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0004_auto_20221210_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='owner',
        ),
    ]
