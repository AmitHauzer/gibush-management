# Generated by Django 4.1.3 on 2022-12-03 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_clinic_note_alter_clinic_health_declaration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='clinic_status',
            field=models.CharField(choices=[('Fit', 'Fit'), ('Unfit', 'Unfit')], default='Fit', editable=False, max_length=50),
        ),
    ]
