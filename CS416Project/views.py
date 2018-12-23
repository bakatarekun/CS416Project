import simplejson as simplejson
from django.core.serializers import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect

from .models import People, SI_Session, Tutor, Schedule, Timetable
from django.core import serializers
# Create your views here.

from django import template



def login_redirect(request):
    return redirect('/login')


def tutorInfo(request, tutor_id):
    tinfo = get_object_or_404(Tutor, pk=tutor_id)

    return render(request, 'tutor_info.html', {'tinfo': tinfo})

def AlltutorsInfo(request):
    info = Tutor.objects.all()

    return render(request, 'tutor_info.html', {'info': info})

def allTutorNames(request, day_of_shift):

    info = Schedule.objects.filter(day=day_of_shift).order_by('tutor__firstname')
    info_jason = serializers.serialize('json', info,  use_natural_foreign_keys=True, )
    # print(info_jason)
    return HttpResponse(info_jason, content_type='application/json')



def showSiBackupbyTutor(request):

    tutorName = request.POST.get('search','')
    day = request.POST.get('search2', '')

    if tutorName=='':
        backupByTutors = SI_Session.objects.filter(day= day).order_by('day','sessionTime_from')
    elif  day=='':
        backupByTutors = SI_Session.objects.filter(tutor__firstname__contains=tutorName).order_by('day','sessionTime_from')
    else:
        backupByTutors = SI_Session.objects.filter( day=day,tutor__firstname__contains=tutorName,).order_by('sessionTime_from')


    return render(request, 'tutor_info.html', {'backupByTutors': backupByTutors,'tutorName': tutorName})


def home(request):

    return render(request, 'home.html')

def location(request):

    return render(request, 'location.html')

def schedule2(request):
    Monday = Timetable.objects.all().filter(day="Monday").order_by('tutor__firstname')
    Tuesday = Timetable.objects.all().filter(day="Tuesday").order_by('tutor__firstname')
    Wednesday = Timetable.objects.all().filter(day="Wednesday").order_by('tutor__firstname')
    Thursday = Timetable.objects.all().filter(day="Thursday").order_by('tutor__firstname')
    Friday = Timetable.objects.all().filter(day="Friday").order_by('tutor__firstname')
    Saturday = Timetable.objects.all().filter(day="Saturday").order_by('tutor__firstname')
    Sunday = Timetable.objects.all().filter(day="Sunday").order_by('tutor__firstname')


    return render(request, 'viewAllSchedule.html', {'Monday': Monday, 'Tuesday': Tuesday, 'Wednesday': Wednesday,'Thursday': Thursday, 'Friday': Friday, 'Saturday': Saturday, 'Sunday': Sunday})



def schedule(request, day):

    usedhours = Schedule.objects.all().filter(day=day)

    for u in usedhours:
        print(str(u.tutor_id) +' '+ u.tutor.firstname)
        count = Timetable.objects.filter(day=day).filter(tutor__firstname = u.tutor.firstname).count()
        # print('count is ' + str(count))
        if count ==  0:
            timetable = Timetable(tutor_id=u.tutor_id, day=u.day, fname=u.tutor.firstname)
            timetable.save()

    tTable = Timetable.objects.all().filter(day=day).order_by('tutor__firstname')
    # print(tTable)
    # print(usedhours)
    zipdata = zip(tTable,usedhours)
    print(zipdata)

    return render(request, 'mathSchedule.html',{'usedhours': usedhours,'day':day, 'schedule': tTable,'zip':zipdata})





def showSiBackupPlan(request, day):

    ti = Tutor.objects.all()
    if day == 'alldays':
        backupPlans = SI_Session.objects.all().order_by('day','sessionTime_from')
    else:
        backupPlans = SI_Session.objects.filter(day=day)
    return render(request, 'showSiBackupPlan.html', {'backupPlans': backupPlans,'ti':ti})

@csrf_protect
def saveUsedHours(request):
    usedhours = request.GET.get('usedhours', 0.0)
    Name = request.GET.get('name', "")
    Name = Name.strip()
    tutorusedhours = get_object_or_404(Tutor, firstname =Name)
    print(tutorusedhours)
    tutorusedhours.usedhours = usedhours
    tutorusedhours.save(update_fields=["usedhours"])
    return HttpResponse('successfuly saved the hours')

def deleteRow(request):
    tutorId = request.GET.get('tutorId', 0)
    scheduleId = request.GET.get('scheduleId', 0)
    timeTableId = request.GET.get('timeTableId', 0)
    usedHrs = float(request.GET.get('usedHrs', ""))

    day = request.GET.get('day', "")

    deletedSchedule = get_object_or_404(Schedule, pk =scheduleId)
    deletedTimetable = get_object_or_404(Timetable, pk=timeTableId)
    deletedSchedule.delete()
    deletedTimetable.delete()
    # print(tutorusedhours)
    tutorToEditHrs = get_object_or_404(Tutor, pk=tutorId)
    temHrs = 0.0
    temHrs=tutorToEditHrs.usedhours
    print(str(temHrs))
    print(str(usedHrs))
    tutorToEditHrs.usedhours  = temHrs - usedHrs
    tutorToEditHrs.save(update_fields=["usedhours"])
    url = '/schedule/' + day+'/'
    return redirect(url)

@csrf_protect
def saveSchedule(request):
    schedule = request.GET.getlist('schedule[]')
    tutorname = request.GET.get('tutorname', "")
    day = request.GET.get('day', "")
    tutorname = tutorname.strip()
    timetable = get_object_or_404(Timetable, tutor__firstname =tutorname, day=day)
    # print(timetable)
    print(schedule)
    if(day == 'Friday'):

        timetable.t0930 = schedule[0]
        timetable.t1000 = schedule[1]
        timetable.t1030 = schedule[2]
        timetable.t1100 = schedule[3]
        timetable.t1130 = schedule[4]
        timetable.t1200 = schedule[5]
        timetable.t1230 = schedule[6]
        timetable.t1300 = schedule[7]
        timetable.t1330 = schedule[8]
        timetable.t1400 = schedule[9]
        timetable.t1430 = schedule[10]
        timetable.t1500 = schedule[11]
        timetable.t1530 = schedule[12]
        timetable.t1600 = schedule[13]
        timetable.save(
            update_fields=['t0930', 't1000', 't1030', 't1100', 't1130', 't1200', 't1230', 't1300', 't1330', 't1400',
                           't1430', 't1500', 't1530', 't1600'])
    elif (day == 'Saturday'):

        timetable.t1000 = schedule[0]
        timetable.t1030 = schedule[1]
        timetable.t1100 = schedule[2]
        timetable.t1130 = schedule[3]
        timetable.t1200 = schedule[4]
        timetable.t1230 = schedule[5]
        timetable.t1300 = schedule[6]
        timetable.t1330 = schedule[7]
        timetable.t1400 = schedule[8]
        timetable.t1430 = schedule[9]
        timetable.t1500 = schedule[10]

        timetable.save(
            update_fields=['t1000', 't1030', 't1100', 't1130', 't1200', 't1230', 't1300', 't1330', 't1400',
                           't1430', 't1500'])


    elif (day == 'Sunday'):

        timetable.t1200 = schedule[0]
        timetable.t1230 = schedule[1]
        timetable.t1300 = schedule[2]
        timetable.t1330 = schedule[3]
        timetable.t1400 = schedule[4]
        timetable.t1430 = schedule[5]
        timetable.t1500 = schedule[6]
        timetable.t1530 = schedule[7]
        timetable.t1600 = schedule[8]

        timetable.save(
            update_fields=[ 't1200', 't1230', 't1300', 't1330', 't1400',
                           't1430', 't1500', 't1530', 't1600'])
    else:
        timetable.t0930 = schedule[0]
        timetable.t1000 = schedule[1]
        timetable.t1030 = schedule[2]
        timetable.t1100 = schedule[3]
        timetable.t1130 = schedule[4]
        timetable.t1200 = schedule[5]
        timetable.t1230 = schedule[6]
        timetable.t1300 = schedule[7]
        timetable.t1330 = schedule[8]
        timetable.t1400 = schedule[9]
        timetable.t1430 = schedule[10]
        timetable.t1500 = schedule[11]
        timetable.t1530 = schedule[12]
        timetable.t1600 = schedule[13]
        timetable.t1630 = schedule[14]
        timetable.t1700 = schedule[15]
        timetable.t1730 = schedule[16]
        timetable.t1800 = schedule[17]
        timetable.t1830 = schedule[18]
        timetable.t1900 = schedule[19]
        timetable.t1930 = schedule[20]
        timetable.t2000 = schedule[21]
        timetable.t2030 = schedule[22]
        timetable.t2100 = schedule[23]

        timetable.save(
            update_fields=['t0930', 't1000', 't1030', 't1100', 't1130', 't1200', 't1230', 't1300', 't1330', 't1400',
                           't1430', 't1500', 't1530', 't1600', 't1630', 't1700', 't1730', 't1800', 't1830', 't1900',
                           't1930', 't2000', 't2030', 't2100'])

    return HttpResponse('successfuly saved the hours')
