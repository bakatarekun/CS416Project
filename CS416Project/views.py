from django.core.serializers import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import People, SI_Session, Tutor
from django.contrib.auth import update_session_auth_hash
from django.core import serializers
# Create your views here.

def login_redirect(request):
    return redirect('/login')


def tutorInfo(request, tutor_id):
    tinfo = get_object_or_404(Tutor, pk=tutor_id)

    return render(request, 'tutor_info.html', {'tinfo': tinfo})

def AlltutorsInfo(request):
    info = Tutor.objectsjects.all()


    return render(request, 'tutor_info.html', {'info': info})

def allTutorNames(request):
    info = Tutor.objects.only("firstname")
    #info = Tutor.objects.filter(lastname= "Yamanaka").order_by('firstname')
    print(info)
    info_jason = serializers.serialize('json', info)
   #info={'info':"hello"}


    #return JsonResponse(info, safe=False)
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

