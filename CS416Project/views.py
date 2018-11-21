from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponse
from .models import People, SI_Session, Tutor
from django.contrib.auth import update_session_auth_hash
# Create your views here.


def tutorInfo(request, tutor_id):
    tutorInfo = get_object_or_404(Tutor, pk=tutor_id)

    return render(request, 'tutor_info.html', {'tutorInfo': tutorInfo})



def home(request):

    return render(request, 'home.html')




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

