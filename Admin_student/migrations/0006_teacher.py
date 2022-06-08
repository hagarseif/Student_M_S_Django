# Generated by Django 4.0.3 on 2022-06-08 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_student', '0005_subject_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('t_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('t_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=11)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin_student.subject')),
            ],
        ),
    ]
