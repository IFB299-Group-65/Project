#render library for returning views to the browser
from django.shortcuts import render
#decorator to make a function only accessible to registered users
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#import the user library
from pusher import pusher
#replace the xxx with your app_id, key and secret respectively
#instantate the pusher class
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
    return render(request,"chat.html"); 
@csrf_exempt
def broadcast(request):
    pusher_client.trigger('my-channel', 'my-event', {u'name': request.user.username, u'message': request.POST['message']})
    return HttpResponse("done");
