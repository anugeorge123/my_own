# Generated by Django 2.2.2 on 2019-10-26 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20191026_0740'),
    ]

    operations = [
        migrations.AddField(
            model_name='realuser',
            name='token',
            field=models.CharField(default='111', max_length=1000, null=True),
        ),
    ]