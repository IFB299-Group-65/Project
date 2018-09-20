# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

def email(request):

    subject = 'Lost Property at Car Rental Company'
    message = 'Hi, \n\nWe found your belongings from the last car that you rent from CRC, Please call us to schedule your pick up time. Thank You.\n\nRegards, \n\nCRC Manager'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['kiki.mutiara49@yahoo.com',]

    send_mail( subject, message, email_from, recipient_list )

    return HttpResponse('<h1>Email sent!</h1>')