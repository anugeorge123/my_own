# Generated by Django 2.2.6 on 2019-10-23 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='steps',
        ),
    ]