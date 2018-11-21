from django.db import models

# Create your models here.
class People(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    age = models.IntegerField()

    def __str__(self):
        return "{self.first_name}"


# class Question(models.Model):
#     question_text = models.CharField(max_length=100)
#     pub_date = models.DateTimeField('date published')
#
#     def __str__(self):
#         return self.question_text
#
#
# class Choice(models.Model):
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.choice_text
#
#     class Meta:  # order by desc
#         ordering = ['-votes']


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

    day = models.CharField(max_length=50)
    tutor = models.ForeignKey(Tutor,on_delete=models.SET_NULL, null=True)
    backup = models.CharField(max_length=50, blank=True)
    sessionTime_from = models.CharField(max_length=50, default='')
    sessionTime_to = models.CharField(max_length=50, default='')
    room = models.CharField(max_length=50,default='')
    professor = models.CharField(max_length=50)
    crn = models.CharField(max_length=50)
    notes = models.CharField(max_length=50,blank=True)
    floor = models.CharField(max_length=50, default='', blank=True)


    def __str__(self):
        return 'CRN:' + self.crn +' ' + self.day + self.sessionTime_from + '-' + self.sessionTime_to

    class Meta: #order by desc
         # ordering = ['sessionTime_from']
         ordering = ['day','sessionTime_from']
