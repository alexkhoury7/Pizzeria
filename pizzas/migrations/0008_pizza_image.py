# Generated by Django 3.0.5 on 2022-12-11 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0007_auto_20221211_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]