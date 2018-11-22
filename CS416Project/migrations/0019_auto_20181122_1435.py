# Generated by Django 2.1.3 on 2018-11-22 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS416Project', '0018_auto_20181122_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='si_session',
            name='sessionTime_from',
            field=models.CharField(choices=[('', '--------'), ('9:30', '9:30'), ('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'), ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '1:00'), ('13:30', '1:30'), ('14:00', '2:00'), ('14:30', '2:30'), ('15:00', '3:00'), ('15:30', '3:30'), ('16:00', '4:00'), ('16:30', '4:30'), ('17:00', '5:00'), ('17:30', '5:30'), ('18:00', '6:00'), ('18:30', '6:30'), ('19:00', '7:00'), ('19:30', '7:30'), ('20:00', '8:00'), ('20:30', '8:30')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='si_session',
            name='sessionTime_to',
            field=models.CharField(choices=[('', '--------'), ('9:30', '9:30'), ('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'), ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '1:00'), ('13:30', '1:30'), ('14:00', '2:00'), ('14:30', '2:30'), ('15:00', '3:00'), ('15:30', '3:30'), ('16:00', '4:00'), ('16:30', '4:30'), ('17:00', '5:00'), ('17:30', '5:30'), ('18:00', '6:00'), ('18:30', '6:30'), ('19:00', '7:00'), ('19:30', '7:30'), ('20:00', '8:00'), ('20:30', '8:30')], default='', max_length=50),
        ),
    ]
