# Generated by Django 2.1.3 on 2018-11-21 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS416Project', '0008_auto_20181121_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='si_session',
            name='day',
            field=models.CharField(choices=[('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday'), ('5', 'Saturday'), ('6', 'Sunday')], max_length=50),
        ),
    ]
