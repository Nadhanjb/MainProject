# Generated by Django 3.2.22 on 2024-02-16 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_data_app', '0002_auto_20240211_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital_table',
            name='proof',
            field=models.FileField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
