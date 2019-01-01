"""CS416Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^home$', views.home, name='home'),
    url(r'^submissionMessage$', views.submissionMessage, name='submissionMessage'),
    url(r'^schedule2$', views.schedule2, name="schedule2"),
    url(r'^deleteRow$', views.deleteRow, name="deleteRow"),
    path('schedule/<day>/', views.schedule, name="schedule"),
    path('allTutorsNames/<day_of_shift>', views.allTutorNames, name='allTutorNames'),
    url(r'^location$', views.location, name="location"),
    url(r'^saveUsedHours$', views.saveUsedHours, name="saveUsedHours"),
    url(r'^saveSchedule$', views.saveSchedule, name="saveSchedule"),
    url(r'^showSiBackupPlanByTutor$', views.showSiBackupbyTutor, name="showSiBackupbyTutor"),
    path('showSiBackupPlan/<day>', views.showSiBackupPlan, name="showSiBackupPlan"),
    url(r'^(?P<tutor_id>[0-9]+)/tutor$', views.tutorInfo, name="tutor"),
    url(r'^tutors/$', auth_views.LoginView.as_view(), name='tutors'),
    path('CS416Project/', include('django.contrib.auth.urls')),
]
