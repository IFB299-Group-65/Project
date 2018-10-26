"""CRCsystems URL Configuration

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
from django.urls import path
    
from . import views

from datetime import datetime
import django.contrib.auth.views
#from pusherchat import views

#import pusherchat.views

import app.forms
from app.views import *

urlpatterns = [
    path('', app.views.home, name='home'),
    path('home.html/', app.views.home, name='home'),
    #path('sendEmail/', include('sendEmail.urls')),
    path('booking.html/', app.views.booking, name='booking'),
    path('payment.html/', app.views.payment, name='payment'),
    path('price.html/', app.views.price, name='price'),
    path('terms-and-conditions.html/', app.views.terms, name='terms'),
    path('tracking.html/', app.views.tracking, name='tracking'),
    path('login.html/report.html/', app.views.report, name='report'),
    path('login.html/', app.views.login, name='login'),
    path('last_service.html/', app.views.last_service, name='last_serviced'),
	path('ajax/chat/', views.broadcast),
    path('chat/', views.chat),
    path('cardetails.html/', app.views.car_details, name='caardetails'),
#    path('^chat$', pusherchat.views.chat),
#    path('^ajax/chat/$', pusherchat.views.broadcast),
#    path('^admin/', admin.site.urls),
]


