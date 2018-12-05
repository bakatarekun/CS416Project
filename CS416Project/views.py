import simplejson as simplejson
from django.core.serializers import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect

from .models import People, SI_Session, Tutor, Schedule
from django.core import serializers
# Create your views here.

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
    print(info_jason)
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

    return render(request, 'mathSchedule.html',{})


def schedule(request, day):
    usedhours = Schedule.objects.all().filter(day=day)
    return render(request, 'mathSchedule.html',{'usedhours': usedhours,'day':day})

def showSiBackupPlan(request):

    ti = Tutor.objects.all()
    monday = SI_Session.objects.filter(day='Monday')
    tuesday = SI_Session.objects.filter(day='Tuesday')
    wednesday = SI_Session.objects.filter(day='Wednesday')
    thursday = SI_Session.objects.filter(day='Thursday')
    singleday = SI_Session.objects.filter(day='Monday').first()
    print(monday)
    return render(request, 'showSiBackupPlan.html', {'monday': monday,'tuesday':tuesday,'wednesday': wednesday,'thursday':thursday, 'singleday':singleday, 'ti':ti})

@csrf_protect
def saveUsedHours(request):
    usedhours = request.GET.get('usedhours', 0.0)
    Name = request.GET.get('name', "")
    tutorusedhours = get_object_or_404(Tutor, firstname =Name)
    print(tutorusedhours)
    tutorusedhours.usedhours = usedhours
    tutorusedhours.save(update_fields=["usedhours"])
    return HttpResponse('successfuly saved the hours')
