"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def email(request):
    """Sends email automatically"""
    subject = 'Lost Property at Car Rental Company'
    message = 'Hi, \n\nWe found your belongings from the last car that you rent from CRC, Please call us to schedule your pick up time. Thank You.\n\nRegards, \n\nCRC Manager'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['kiki.mutiara49@yahoo.com',]

    send_mail( subject, message, email_from, recipient_list )

    return HttpResponse('<h1>Email sent!</h1>')
