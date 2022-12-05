# Generated by Django 4.1.3 on 2022-12-03 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('soldiers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health_declaration', models.FileField(max_length=254, upload_to=None)),
                ('clinic_status', models.CharField(choices=[('Open', 'Open'), ('Fit', 'Fit'), ('Unfit', 'Unfit')], default='Open', editable=False, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('soldier', models.OneToOneField(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='soldiers.soldier')),
            ],
        ),
    ]