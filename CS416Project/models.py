import calendar
import array
from django.db import models

# Create your models here.
class People(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    age = models.IntegerField()

    def __str__(self):
        return "{self.first_name}"

class Tutor(models.Model):

    firstname = models.CharField(max_length=50,default='')
    lastname = models.CharField(max_length=50,default='')
    hours = models.IntegerField(default=0)
    subject1 = models.CharField(max_length=50, default='', null=True)
    subject2 = models.CharField(max_length=50, default='', null=True)


    def __str__(self):
        return self.firstname + self.lastname

    class Meta: #order by desc
         ordering = ['firstname']


class SI_Session(models.Model):


    # room_choices = [(str(i),rooms[i]) for i in range(0, 2)]
    # day_choices = [(str(i),calendar.day_name[i]) for i in range(0, 7)]
    day_choices = (
        ('', '--------'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Sarturday', 'Satruday'),
        ('Sunday', 'Sunday'),

    )

    room_choices = (
        ('', '--------'),
        ('blue', 'blue'),
        ('yellow', 'yellow'),
        ('pink', 'pink'),

    )

    time_choices = (
        ('', '--------'),
        ('9:30', '9:30'),
        ('10:00', '10:00'),
        ('10:30', '10:30'),
        ('11:00', '11:00'),
        ('11:30', '11:30'),
        ('12:00', '12:00'),

    )
    day = models.CharField(max_length=50, choices=day_choices)
    tutor = models.ForeignKey(Tutor,on_delete=models.SET_NULL, null=True)
    backup = models.CharField(max_length=50, blank=True)
    sessionTime_from = models.CharField(max_length=50, default='', choices=time_choices)
    sessionTime_to = models.CharField(max_length=50, default='', choices=time_choices)
    room = models.CharField(max_length=50,default='',choices=room_choices)
    professor = models.CharField(max_length=50)
    crn = models.CharField(max_length=50)
    notes = models.CharField(max_length=50,blank=True)
    floor = models.CharField(max_length=50, default='', blank=True)


    def __str__(self):
        return 'CRN:' + self.crn +' ' + self.day + self.sessionTime_from + '-' + self.sessionTime_to

    class Meta: #order by desc
         # ordering = ['sessionTime_from']
         ordering = ['day','sessionTime_from']
