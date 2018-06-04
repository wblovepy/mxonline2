# Generated by Django 2.0 on 2018-05-13 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizition', '0006_courseorg_course_num'),
        ('course', '0004_auto_20180510_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='org_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organizition.CourseOrg', verbose_name='所属机构'),
        ),
    ]