# Generated by Django 4.1 on 2022-09-06 15:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_deposit_date_alter_myuser_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 6, 16, 24, 55, 245386)),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 6, 16, 24, 55, 245386)),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='dob',
            field=models.DateField(default=datetime.datetime(2022, 9, 6, 15, 24, 55, 245386, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='others',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 6, 16, 24, 55, 245386)),
        ),
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 6, 16, 24, 55, 245386)),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 6, 16, 24, 55, 245386)),
        ),
        migrations.AlterField(
            model_name='withdrawal_page',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 6, 16, 24, 55, 245386)),
        ),
    ]
