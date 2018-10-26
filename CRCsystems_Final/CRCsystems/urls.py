#"""
#Definition of urls for CRCSystems.
#"""
#
#from datetime import datetime
#from django.conf.urls import url, include
#import django.contrib.auth.views
#from pusherchat import views
#from django.contrib import admin
#
#import pusherchat.views
#
#import app.forms
#import app.views
#
## Uncomment the next lines to enable the admin:
## from django.conf.urls import include
## from django.contrib import admin
## admin.autodiscover()
#
#urlpatterns = [
#    url(r'^$', app.views.home, name='home'),
#    url(r'^home.html$', app.views.home, name='home'),
#    url(r'^sendEmail/', include('sendEmail.urls')),
#    url(r'^booking.html$', app.views.booking, name='booking'),
#    url(r'^payment.html$', app.views.payment, name='payment'),
#    url(r'^price.html$', app.views.price, name='price'),
#    url(r'^terms-and-conditions.html$', app.views.terms, name='terms'),
#    url(r'^tracking.html$', app.views.tracking, name='tracking'),
#    url(r'^chat$', pusherchat.views.chat),
#    url(r'^ajax/chat/$', pusherchat.views.broadcast),
#    url(r'^admin/', admin.site.urls),
#    
#    # Uncomment the admin/doc line below to enable admin documentation:
#    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#
#    # Uncomment the next line to enable the admin:
#    # url(r'^admin/', include(admin.site.urls)),
#]
