# Generated by Django 5.1.3 on 2024-11-27 15:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='enrolment_name',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]