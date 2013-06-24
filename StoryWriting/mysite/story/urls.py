from django.conf.urls import patterns, url
from story import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^fullstory$', views.fullstory, name='fullstory'),
    url(r'^addstory$', views.addstory, name='addstory'),
    url(r'^chkuser$', views.chkuser, name='chkuser'),
    url(r'^adduser$', views.adduser, name='adduser'),
    url(r'^admin$', views.tadmin, name='tadmin'),
    url(r'^prework$', views.prework, name='prework'),
    url(r'^time$', views.ttime, name='ttime'),
    url(r'^starter$', views.starter, name='starter'),
    url(r'^viewstory$', views.viewstory, name='viewstory'),
    url(r'^[A-Za-z0-9][A-Za-z0-9][A-Za-z0-9]$', views.tuser, name='tuser')
    
)
