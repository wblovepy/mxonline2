# Generated by Django 2.0 on 2018-05-07 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizition', '0004_auto_20180506_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='student',
            field=models.IntegerField(default=0, verbose_name='学生数'),
        ),
    ]
