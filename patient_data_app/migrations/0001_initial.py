# Generated by Django 3.2.22 on 2024-02-11 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dept_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=50)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='doctor_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=35)),
                ('dob', models.DateField()),
                ('place', models.CharField(max_length=50)),
                ('pin', models.BigIntegerField()),
                ('post', models.CharField(max_length=30)),
                ('phone', models.BigIntegerField()),
                ('email', models.CharField(max_length=50)),
                ('qualification', models.TextField()),
                ('specialization', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=100)),
                ('photo', models.FileField(upload_to='')),
                ('DEPARTMENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_data_app.dept_table')),
            ],
        ),
        migrations.CreateModel(
            name='login_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='patient_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=35)),
                ('dob', models.DateField()),
                ('place', models.CharField(max_length=50)),
                ('pin', models.BigIntegerField()),
                ('post', models.CharField(max_length=30)),
                ('phone', models.BigIntegerField()),
                ('email', models.CharField(max_length=50)),
                ('photo', models.FileField(upload_to='')),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_data_app.login_table')),
            ],
        ),
        migrations.CreateModel(
            name='medical_record_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=20)),
                ('test_name', models.CharField(max_length=30)),
                ('test_result', models.FileField(upload_to='')),
                ('test_result_conclusion', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('DOCTOR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_data_app.doctor_table')),
                ('PATIENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_data_app.patient_table')),
            ],
        ),
        migrations.CreateModel(
            name='hospital_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hosp_name', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField()),
                ('email', models.CharField(max_length=50)),
                ('license_no', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_data_app.login_table')),
            ],
        ),
        migrations.AddField(
            model_name='doctor_table',
            name='LOGIN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_data_app.login_table'),
        ),
        migrations.AddField(
            model_name='dept_table',
            name='HOSPITAL',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_data_app.hospital_table'),
        ),
        migrations.CreateModel(
            name='appointment_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=30)),
                ('DOCTOR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_data_app.doctor_table')),
                ('PATIENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_data_app.patient_table')),
            ],
        ),
    ]
