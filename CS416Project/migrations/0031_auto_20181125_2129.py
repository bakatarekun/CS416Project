# Generated by Django 2.1.3 on 2018-11-25 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CS416Project', '0030_auto_20181125_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='hours',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='lastname',
        ),
        migrations.AddField(
            model_name='schedule',
            name='tutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CS416Project.Tutor'),
        ),
    ]
