"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect

from app.models import *

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/home.html',
    )

def price(request):
    """Renders the price page."""
    assert isinstance(request, HttpRequest)
    f = ''
    if(request.GET.get('Submit')):
        f = Car.objects.filter(car_makename=request.GET.get('car_make'))
    return render(
        request,
        'app/price.html',
        {'filter' : f},
    )

def payment(request):
    """Renders the payment page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/payment.html',
    )

def booking(request):
    """Renders the booking page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/booking.html',
    )

def terms(request):
    """Renders the terms and condition page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/terms-and-conditions.html',
    )

def tracking(request):
    """Renders the tracking page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/tracking.html',
    )

def report(request):
    """Render Car report page"""
    assert isinstance(request, HttpRequest)
    o = ''
    if(request.GET.get('mybtn')):
        if(request.GET.get('method') == 'Picked Up'):
            o = Orders.objects.filter(order_pickupdate__month=int(request.GET.get('month')))
        
        #o = Order.objects.filter(method=request.GET.get('method'), location=request.GET.get('location'), pub_date__month=int(request.GET.get('month')))
        o = str(len(o))
#        o = Order.objects.all()
    return render(
        request, 
        'app/report.html',
        {'o': o},
    )

def login(request):
    """Render Car report page"""
    assert isinstance(request, HttpRequest)
    o = 0
    if(request.GET.get('Submit')):
        o = AuthUser.objects.filter(username=request.GET.get('username'), password=make_password(request.GET.get('password'), '1'))
        o = (len(o) == 1)
        
        return HttpResponseRedirect('report.html')
    return render(
        request, 
        'app/login.html',
    )

