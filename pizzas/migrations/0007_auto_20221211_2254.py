# Generated by Django 3.0.5 on 2022-12-11 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0006_auto_20221211_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=200),
        ),
    ]
