# Generated by Django 2.2.2 on 2019-10-26 07:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_remove_recipe_steps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cook',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prep',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='yields',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
