from django.shortcuts import render, get_object_or_404, redirect
from django.http import  HttpResponse
from .models import People, SI_Session, Tutor
from django.contrib.auth import update_session_auth_hash
# Create your views here.

def login_redirect(request):
    return redirect('/login')


def tutorInfo(request, tutor_id):
    tutorInfo = get_object_or_404(Tutor, pk=tutor_id)

    return render(request, 'tutor_info.html', {'tutorInfo': tutorInfo})

#
# def showSiBakcupbyTutor(request, tutor_name):
#     # backupByTutors = SI_Session.objects.filter(day='Monday', tutor__firstname=tutor_name).order_by('sessionTime_from')
#     backupByTutors = SI_Session.objects.filter(day= 'Monday', tutor__firstname__contains=tutor_name).order_by('sessionTime_from')
#
#     return render(request,'tutor_info.html', {'backupByTutors': backupByTutors})


def showSiBakcupbyTutor(request):
    # backupByTutors = SI_Session.objects.filter(day='Monday', tutor__firstname=tutor_name).order_by('sessionTime_from')

        tutorName = request.POST.get('search','')
        day = request.POST.get('search2', '')
        if(tutorName==''):
            backupByTutors = SI_Session.objects.filter(day= day).order_by('day','sessionTime_from')
        elif (day==''):
            backupByTutors = SI_Session.objects.filter(tutor__firstname__contains=tutorName).order_by('day','sessionTime_from')
        else:
            backupByTutors = SI_Session.objects.filter(tutor__firstname__contains=tutorName,day=day).order_by('sessionTime_from')
        return render(request, 'tutor_info.html', {'backupByTutors': backupByTutors, 'day':day})


def home(request):

    return render(request, 'home.html')

def schedule(request):

    return render(request, 'mathSchedule.html')



def showSiBackupPlan(request):

    # monday = SI_Session.objects.filter(day='Monday').order_by('sessionTime_from')
    #
    # tuesday = SI_Session. objects.filter(day='Tuesday').order_by('sessionTime_from')
    # wednesday = SI_Session.objects.filter(day='Wednesday').order_by('sessionTime_from')
    # thursday = SI_Session. objects.filter(day='Thursday').order_by('sessionTime_from')
    monday = SI_Session.objects.filter(day='Monday')

    tuesday = SI_Session.objects.filter(day='Tuesday')
    wednesday = SI_Session.objects.filter(day='Wednesday')
    thursday = SI_Session.objects.filter(day='Thursday')
    singleday = SI_Session.objects.filter(day='Monday').first()
    return render(request, 'showSiBackupPlan.html', {'monday': monday,'tuesday':tuesday,'wednesday': wednesday,'thursday':thursday, 'singleday':singleday})

