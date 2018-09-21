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
    return render(
        request,
        'app/price.html',
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

