import decimal

# import simplejson as simplejson
# from django.core.serializers import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView
from CS416Project.forms import HomeForm,NameForm
from .models import People, SI_Session, Tutor, Schedule, Timetable
from django.core import serializers
from django.contrib.auth.decorators import user_passes_test


def user_check(user):
    return user.username == 'bakatarekun'


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self,request):
        form = HomeForm(prefix="form")
        form2 = HomeForm(prefix="form2")
        form3 = HomeForm(prefix="form3")
        form4 = HomeForm(prefix="form4")
        form5 = HomeForm(prefix="form5")
        form6 = HomeForm(prefix="form6")
        form7 = HomeForm(prefix="form7")
        nameform = NameForm()
        print('get is fired')
        return render(request, self.template_name,{'form':form,'form2':form2,'form3':form3,'form4':form4,'form5':form5,'form6':form6,'form7':form7,'nameform':nameform})

    def post(self, request):

        form = HomeForm(request.POST, prefix="form")
        if form.is_valid():
            from1value = form.cleaned_data['From1']

            if from1value != '0':
                form.save()

        form2 = HomeForm(request.POST, prefix="form2")
        if form2.is_valid():
            from1value2 = form2.cleaned_data['From1']

            if from1value2 != '0':
                form2.save()

        form3 = HomeForm(request.POST, prefix="form3")
        if form3.is_valid():
            from1value3 = form.cleaned_data['From1']

            if from1value3 != '0':
                form3.save()

        form4 = HomeForm(request.POST, prefix="form4")
        if form4.is_valid():
            from1value4 = form4.cleaned_data['From1']

            if from1value4 != '0':
                form4.save()

        form5 = HomeForm(request.POST, prefix="form5")
        if form5.is_valid():
            from1value5 = form5.cleaned_data['From1']

            if from1value5 != '0':
                form5.save()

        form6 = HomeForm(request.POST, prefix="form6")
        if form6.is_valid():
            from1value6 = form6.cleaned_data['From1']

            if from1value6 != '0':
                form6.save()

        form7 = HomeForm(request.POST, prefix="form7")
        if form7.is_valid():
            from1value7 = form7.cleaned_data['From1']

            if from1value7 != '0':
                form7.save()

            form = HomeForm()
            return redirect('submissionMessage')

        args = {'form': form,'form2': form2,'form3': form3,'form4': form4,'form5': form5,'form6': form6,'form7': form7, }
        # args = {'form':form,'text':text,'from1':from1,'to1':to1,'day':day}
        return render(request, self.template_name, args)

def submissionMessage(request):
    return render(request, 'submissionMessage.html', {})

def home(request):
    homeview = HomeView()
    # return render(request, 'home.html')
    if(request.method =='POST'):
        return homeview.post(request)
    else:
        return homeview.get(request)
    # return homeview.get(request)


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


@user_passes_test(user_check,login_url='/login')
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
    usedHrs = decimal.Decimal(request.GET.get('usedHrs', ""))
    day = request.GET.get('day', "")
    deletedSchedule = get_object_or_404(Schedule, pk =scheduleId)
    deletedTimetable = get_object_or_404(Timetable, pk=timeTableId)
    deletedSchedule.delete()
    deletedTimetable.delete()
    tutorToEditHrs = get_object_or_404(Tutor, pk=tutorId)
    tutorToEditHrs.usedhours  = tutorToEditHrs.usedhours - usedHrs
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
