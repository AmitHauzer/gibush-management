# Generated by Django 4.1.3 on 2022-11-20 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Soldier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('soldier_status', models.CharField(default='Waiting for Baror', max_length=50)),
            ],
        ),
    ]