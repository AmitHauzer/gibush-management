# Generated by Django 4.1.3 on 2022-12-02 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('soldiers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shalishut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity_num', models.CharField(blank=True, max_length=9, null=True)),
                ('firstname', models.CharField(blank=True, max_length=20, null=True)),
                ('lastname', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('profile', models.IntegerField(blank=True, choices=[(97, '97'), (82, '82'), (72, '72')], null=True)),
                ('shalishut_status', models.CharField(choices=[('Open', 'Open'), ('Done', 'Done')], default='Open', editable=False, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('soldier', models.OneToOneField(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='soldiers.soldier')),
            ],
        ),
    ]
