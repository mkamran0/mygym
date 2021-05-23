# Generated by Django 3.1.7 on 2021-05-21 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210521_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='address',
        ),
        migrations.AddField(
            model_name='contact',
            name='category',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='contact',
            name='gender',
            field=models.CharField(default='', max_length=10),
        ),
    ]
