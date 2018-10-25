from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect

from polls.models import *

def last_service(request):
    assert isinstance(request, HttpRequest)
    data = ''
    if(request.GET.get('submit')):
       data = Carservice.objects.filter(car_id = request.GET.get('Car_ID'))
       data = data[0]
    return render(
        request,
        'PAGE.html',
        {'data' : data},
    )
    
