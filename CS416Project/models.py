import calendar
import array
from django.db import models

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

class TutorManager(models.Manager):
    def get_by_natural_key(self, firstname, lastname):
        return self.get(firstname=firstname, lastname=lastname)

class Tutor(models.Model):

    objects = TutorManager()

    firstname = models.CharField(max_length=50,default='')
    lastname = models.CharField(max_length=50,default='')
    hours = models.IntegerField(default=0)
    typeofstaff = models.CharField(max_length=50, default='',choices=type_choices)
    subject1 = models.CharField(max_length=50, default='', null=True, choices=subject_choices)
    subject2 = models.CharField(max_length=50, default='', null=True, blank=True,choices=subject_choices)
    usedhours = models.DecimalField(decimal_places=1, max_digits=3, default=0)

    def natural_key(self):
        return (self.firstname, self.typeofstaff, self.hours,self.usedhours)


    def __str__(self):
        return self.firstname + ' '+ self.lastname

    class Meta: #order by desc
         ordering = ['firstname']
         unique_together = (('firstname', 'lastname'),)


class Timetable(models.Model):

    tutor = models.ForeignKey(Tutor, on_delete=models.SET_NULL, null=True)
    day = models.CharField(max_length=50, default='',choices=day_choices)
    t0930 = models.CharField(max_length=10, blank=True, default='', null=True)
    t1000 =models.CharField(max_length=10, blank=True, default='', null=True )
    t1030 = models.CharField(max_length=10, blank=True, default='', null=True)
    t1100 = models.CharField(max_length=10, blank=True, default='', null=True)
    t1130 = models.CharField(max_length=10, blank=True, default='', null=True)
    t1200 = models.CharField(max_length=10, blank=True, default='', null=True)
    t1230 = models.CharField(max_length=10, blank=True, default='', null=True)
    t1300 = models.CharField(max_length=10, blank=True, default='', null=True)
    t1330 = models.CharField(max_length=10, blank=True, default='', null=True)
    t1400 =models.CharField(max_length=10, blank=True, default='', null=True)
    t1430 =models.CharField(max_length=10, blank=True, default='', null=True)
    t1500 = models.CharField(max_length=10, blank=True, default='', null=True)
    t1530 =models.CharField(max_length=10, blank=True, default='', null=True)
    t1600 = models.CharField(max_length=10, blank=True, default='', null=True)
    t1630 = models.CharField(max_length=10, blank=True, default='', null=True)
    t1700 = models.CharField(max_length=10, blank=True, default='', null=True)
    t1730 = models.CharField(max_length=10, blank=True, default='', null=True)
    t1800 =models.CharField(max_length=10, blank=True, default='', null=True)
    t1830 = models.CharField(max_length=10, blank=True, default='', null=True)
    t1900 = models.CharField(max_length=10, blank=True, default='', null=True)
    t1930 =models.CharField(max_length=10, blank=True, default='', null=True)
    t2000 =models.CharField(max_length=10, blank=True, default='', null=True)
    t2030 =models.CharField(max_length=10, blank=True, default='', null=True)
    t2100 =models.CharField(max_length=10, blank=True, default='', null=True)

    def __str__(self):
        return self.day

# Create your models here.
class People(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    age = models.IntegerField()

    def __str__(self):
        return "{self.first_name}"






class SI_Session(models.Model):

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
                 ordering = ['day','sessionTime_from']



class Schedule(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.SET_NULL, null=True)
    day = models.CharField(max_length=50, default='',choices=day_choices)
    From1 = models.CharField(max_length=50, default='',choices=time_choices)
    To1 = models.CharField(max_length=50, default='', choices=time_choices)
    From2 = models.CharField(max_length=50, default='',blank=True,choices=time_choices)
    To2 = models.CharField(max_length=50, default='',blank=True,choices=time_choices)
    usedhours = models.DecimalField(decimal_places=1, max_digits=3,default=0)



    def __str__(self):
        return self.tutor.firstname + ' '+ self.tutor.lastname + ' '+ self.day + ' ' + str(self.usedhours)

    class Meta:  # order by desc
        ordering = ['day', 'tutor__firstname']


 # from django import template
 #    register = template.Library()
 #
 #    @register.filter
 #    def state_css_class(value):
 #        """returns appropriate bootstrap label class for states"""
 #        statemap = {
 #            'Ken': 'eacellcolor',
 #            'Alisha': 'sacellcolor',
 #            'Mary': 'wscellcolor',
 #            'Sean': 'eacellcolor',
 #            'Joe': 'wacellcolor',
 #
 #        }
 #        try:
 #            return statemap[value]
 #        except KeyError:
 #            return ' '
