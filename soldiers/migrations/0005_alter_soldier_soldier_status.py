# Generated by Django 4.1.3 on 2022-11-30 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soldiers', '0004_alter_soldier_idf_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldier',
            name='soldier_status',
            field=models.CharField(choices=[('Waiting for Shalishut', 'Waiting for Shalishut'), ('Waiting for Clinic', 'Waiting for Clinic'), ('Waiting for Baror', 'Waiting for Baror'), ('Ready to run', 'Ready to run'), ('Running', 'Running'), ('After Baror', 'After Baror'), ('Medically disqualified', 'Medically disqualified'), ('Active', 'Active'), ('Quit', 'Quit'), ('Pass', 'Pass')], default='Waiting for Shalishut', max_length=50),
        ),
    ]
