# Generated by Django 3.1.7 on 2021-07-17 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_class',
            field=models.CharField(max_length=12),
        ),
    ]
