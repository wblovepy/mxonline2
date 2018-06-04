# Generated by Django 2.0 on 2018-05-10 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20180502_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(choices=[('register', '注册'), ('forget', '忘记密码')], default='', max_length=20, verbose_name='发送验证类型'),
        ),
    ]
