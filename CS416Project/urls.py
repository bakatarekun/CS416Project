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

# from django.urls import path
#from django.conf.urls import include

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^home$', views.home),
    url(r'^(?P<tutor_id>[0-9]+)/tutor$', views.tutorInfo, name="tutorInfo"),

    path('CS416Project/', include('django.contrib.auth.urls')),

    url(r'^showSiBackupPlan/$', views.showSiBackupPlan, name='showSiBackupPlan'),
    # url(r'^test_app/', include('test_app.urls')),
   # path('/', include('django.contrib.auth.urls')),
]
