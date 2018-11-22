# Generated by Django 2.1.3 on 2018-11-21 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS416Project', '0015_auto_20181121_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='si_session',
            name='sessionTime_from',
            field=models.CharField(choices=[('', '--------'), ('9:30', '9:30'), ('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'), ('12:00', '12:00')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='si_session',
            name='sessionTime_to',
            field=models.CharField(choices=[('', '--------'), ('9:30', '9:30'), ('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'), ('12:00', '12:00')], default='', max_length=50),
        ),
    ]
