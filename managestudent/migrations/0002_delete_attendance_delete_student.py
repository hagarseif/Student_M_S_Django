# Generated by Django 4.0.3 on 2022-06-08 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managestudent', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='attendance',
        ),
        migrations.DeleteModel(
            name='student',
        ),
    ]
