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

#decorator to make a function only accessible to registered users
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt
#import the user library
from pusher import pusher

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
            o = Orders.objects.filter(order_pickupdate__month=int(request.GET.get('month')), order_pickupstore=int(request.GET.get('location')))
        else:
            o = Orders.objects.filter(order_returndate__month=int(request.GET.get('month')))

        o = str(len(o))
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
        if(o):
            return HttpResponseRedirect('report.html')
    return render(
        request, 
        'app/login.html',
    )

def last_service(request):
    assert isinstance(request, HttpRequest)
    data = ''
    if(request.GET.get('submit')):
        data = Carservice.objects.filter(car_id = request.GET.get('Car_ID'))
        data = data[len(data) - 1]
    return render(
        request,
        'app/last_service.html',
        {'data' : data},
    )

def car_details(request):
    assert isinstance(request, HttpRequest)
    details = Car.objects.all()
    return render(
        request,
        'app/cardetails.html',
        {'details' : details},
    )

pusher_client = pusher.Pusher(
    app_id='597530',
    key='5c4a5573f267f6f88bdd',
    secret='3954b602b9ebff2aa117',
    cluster='ap1',
    ssl=True
    )
# Create your views here.
#login required to access this page. will redirect to admin login page.
@login_required(login_url='/admin/login/')
def chat(request):
    return render(request,"app/chat.html"); 
@csrf_exempt
def broadcast(request):
    pusher_client.trigger('my-channel', 'my-event', {u'name': request.user.username, u'message': request.POST.get('message')})
    return HttpResponse("done");

