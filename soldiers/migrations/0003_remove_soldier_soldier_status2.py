# Generated by Django 4.1.3 on 2022-11-20 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soldiers', '0002_soldier_soldier_status2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='soldier',
            name='soldier_status2',
        ),
    ]
