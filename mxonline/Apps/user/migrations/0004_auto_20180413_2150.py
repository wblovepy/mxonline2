# Generated by Django 2.0.4 on 2018-04-13 21:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20180409_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 13, 21, 50, 32, 951641), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 13, 21, 50, 32, 951140)),
        ),
    ]
