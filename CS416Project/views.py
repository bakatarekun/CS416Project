import simplejson as simplejson
from django.core.serializers import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import People, SI_Session, Tutor, Schedule
from django.contrib.auth import update_session_auth_hash
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

def allTutorNames(request):
    #info2 = Schedule.objects.only("tutor").filter(day= "Tuesday")
    #info3 =  Tutor.objects.all()
   # info2_list = list(info2)
    #info = Schedule.objects.select_related()
    #info = Schedule.objects.all()
    #print(info2_list[1].tutor.firstname)
    # for e in info:
    #     print(e.tutor.firstname )
    #     print(e.tutor.hours)
   # info_all = list(info) + list(info3)
    # info_jason = serializers.serialize('json', info, fields=('tutor.firstname'))
   # print(info_jason)
    #info={'info':"hello"}
    # response_dict = {
    #     'info': "Hello"
    # }
    # return HttpResponse(simplejson.dumps(response_dict),mimetype='application/json')
    #return JsonResponse(info, safe=False)
    #info = Schedule.objects.prefetch_related(*joins).all().serialize(*joins)


    info = Schedule.objects.filter(day="Wednesday").order_by('tutor__firstname')
    info_jason = serializers.serialize('json', info,  use_natural_foreign_keys=True, )
    print(info_jason)
    return HttpResponse(info_jason, content_type='application/json')



def showSiBakcupbyTutor(request):

    thisset = {"apple", "banana", "cherry"}
    tutorName = request.POST.get('search','')
    day = request.POST.get('search2', '')

    if tutorName=='':
            backupByTutors = SI_Session.objects.filter(day= day).order_by('day','sessionTime_from')
    elif  day=='':
            backupByTutors = SI_Session.objects.filter(tutor__firstname__contains=tutorName).order_by('day','sessionTime_from')
    else:
            backupByTutors = SI_Session.objects.filter( day=day,tutor__firstname__contains=tutorName,).order_by('sessionTime_from')


    return render(request, 'tutor_info.html', {'backupByTutors': backupByTutors, 'ti': thisset})


def home(request):

    return render(request, 'home.html')

def schedule(request):

    return render(request, 'mathSchedule.html')



def showSiBackupPlan(request):

    ti = Tutor.objects.all()
    monday = SI_Session.objects.filter(day='Monday')
    tuesday = SI_Session.objects.filter(day='Tuesday')
    wednesday = SI_Session.objects.filter(day='Wednesday')
    thursday = SI_Session.objects.filter(day='Thursday')
    singleday = SI_Session.objects.filter(day='Monday').first()
    return render(request, 'showSiBackupPlan.html', {'monday': monday,'tuesday':tuesday,'wednesday': wednesday,'thursday':thursday, 'singleday':singleday, 'ti':ti})

