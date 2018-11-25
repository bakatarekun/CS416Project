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
    type_choices = (
        ('', '--------'),
        ('EA', 'EA'),
        ('SA', 'SA'),
        ('Work Study', 'Work Study'),
        ('Volunteer', 'Volunteer'),

    )

    subject_choices = (
        ('', '--------'),
        ('Math', 'Math'),
        ('English', 'English'),
        ('Biology', 'Biology'),
        ('Chemistry', 'Chemistry'),
        ('Physics', 'Physics'),
        ('Computer', 'Computer'),

    )
    firstname = models.CharField(max_length=50,default='')
    lastname = models.CharField(max_length=50,default='')
    hours = models.IntegerField(default=0)
    typeofstaff = models.CharField(max_length=50, default='',choices=type_choices)
    subject1 = models.CharField(max_length=50, default='', null=True, choices=subject_choices)
    subject2 = models.CharField(max_length=50, default='', null=True, choices=subject_choices)


    def __str__(self):
        return self.firstname + ' '+ self.lastname

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
        ('09:30', '9:30'),
        ('10:00', '10:00'),
        ('10:30', '10:30'),
        ('11:00', '11:00'),
        ('11:30', '11:30'),
        ('12:00', '12:00'),
        ('12:30', '12:30'),
        ('13:00', '1:00'),
        ('13:30', '1:30'),
        ('14:00', '2:00'),
        ('14:30', '2:30'),
        ('15:00', '3:00'),
        ('15:30', '3:30'),
        ('16:00', '4:00'),
        ('16:30', '4:30'),
        ('17:00', '5:00'),
        ('17:30', '5:30'),
        ('18:00', '6:00'),
        ('18:30', '6:30'),
        ('19:00', '7:00'),
        ('19:30', '7:30'),
        ('20:00', '8:00'),
        ('20:30', '8:30'),

    )

    crn_choices = (
        ('', '--------'),
        ('2133', '2134'),
        ('2435', '2435'),
        ('1341', '1341'),
    )

    faculty_choices = (
        ('', '--------'),
        ('Smith', 'Smith'),
        ('Thomas', 'Thomas'),
        ('Daddona', 'Daddona'),
    )

    day = models.CharField(max_length=50, choices=day_choices)
    tutor = models.ForeignKey(Tutor,on_delete=models.SET_NULL, null=True)
    backup = models.CharField(max_length=50, blank=True)
    sessionTime_from = models.CharField(max_length=50,default='', choices=time_choices)
    sessionTime_to = models.CharField(max_length=50,default='', choices=time_choices)
    room = models.CharField(max_length=50,default='',choices=room_choices)
    professor = models.CharField(max_length=50,default='', choices=faculty_choices)
    crn = models.CharField(max_length=50, default='', choices=crn_choices)
    notes = models.CharField(max_length=50,blank=True)
    floor = models.CharField(max_length=50, default='', blank=True)


    def __str__(self):
        return 'CRN:' + self.crn +' ' + self.day + self.sessionTime_from + '-' + self.sessionTime_to + " " + self.tutor.firstname

    class Meta: #order by desc
         # ordering = ['sessionTime_from']
         ordering = ['day','sessionTime_from']
