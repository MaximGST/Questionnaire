# Generated by Django 3.2.6 on 2021-09-02 04:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20210902_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 12, 10, 59, 14, 369265), verbose_name='Дата и время окончание опроса'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 2, 10, 59, 14, 369265), verbose_name='Дата и время начало опроса'),
        ),
        migrations.DeleteModel(
            name='Car',
        ),
    ]