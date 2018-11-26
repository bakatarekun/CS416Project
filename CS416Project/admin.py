from django.contrib import admin

from CS416Project.models import SI_Session, Tutor, Timetable,Schedule

admin.site.register(SI_Session)
admin.site.register(Tutor)
admin.site.register(Schedule)
admin.site.register(Timetable)
