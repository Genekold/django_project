# Generated by Django 5.1.3 on 2024-11-19 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.CharField(choices=[('first', 'Первый курс'), ('second', 'Второй курс'), ('third', 'Третий курс'), ('fourth', 'Четвертый курс')], default='fourth', max_length=6, verbose_name='Курс'),
        ),
    ]