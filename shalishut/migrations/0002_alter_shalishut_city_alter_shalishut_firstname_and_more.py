# Generated by Django 4.1.3 on 2022-12-02 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shalishut', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shalishut',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='shalishut',
            name='firstname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='shalishut',
            name='identity_num',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='shalishut',
            name='lastname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='shalishut',
            name='profile',
            field=models.IntegerField(choices=[(97, '97'), (82, '82'), (72, '72')]),
        ),
    ]
