# Generated by Django 2.1.3 on 2018-12-22 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CS416Project', '0045_auto_20181222_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='timetableId',
            field=models.OneToOneField(blank=True, default='Ken Monday', null=True, on_delete=django.db.models.deletion.SET_NULL, to='CS416Project.Timetable'),
        ),
    ]
