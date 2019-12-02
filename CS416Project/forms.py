from django import forms
from django.forms import Textarea,TextInput

from CS416Project.models import Schedule, Tutor

CHOICES = ( ('', '--------'),
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
tutors = (('1', 'Ken'), ('2', 'Sean'),('3', 'Mary'), ('4', 'Alisha'),('5', 'Joe'),)
day_choices = (

    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),

)
# class HomeForm(forms.Form):
#     post = forms.CharField(max_length=50, widget=forms.TextInput(
#         attrs={'placeholder' : 'Enter to do here'}
#     ))
#
#     tutor = forms.ChoiceField(choices=tutors)
#     from1 = forms.ChoiceField(choices=CHOICES)
#     to1 = forms.ChoiceField(choices=CHOICES)

class TodoFrom(forms.Form):
    # text = forms.CharField(max_length=50, widget=forms.TextInput(
    #     attrs={'placeholder' : 'Enter to do here'}
    # ))

    tutor = forms.IntegerField(widget = forms.Select(
        choices=Tutor.objects.all().values_list('id', 'lastname')
    )
    )
    comment = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your comment here'}
    ))

class HomeForm(forms.ModelForm):
    prefix = 'form'
    # post = forms.CharField(max_length=50, widget=forms.TextInput(
    #     attrs={'placeholder' : 'Enter to do here'}
    # ))

    # tutorid = forms.IntegerField(widget=forms.Select(
    #     choices=Tutor.objects.all().values_list('id', 'lastname')
    # )
    # )

    class Meta:
        model = Schedule
        fields = ('day','tutor', 'From1','To1','From2','To2',)
        
        widgets = {
            'day': TextInput(attrs={'placeholder' : 'Enter to do here'}),

        }

        labels = {
            'tutor': (''),
        }


class NameForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = ('tutor',)
