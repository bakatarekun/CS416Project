# Generated by Django 2.1.3 on 2018-12-23 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CS416Project', '0054_auto_20181223_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='timetableId',
            field=models.ForeignKey(default='Ken Monday', null=True, on_delete=django.db.models.deletion.CASCADE, to='CS416Project.Timetable'),
        ),
    ]
