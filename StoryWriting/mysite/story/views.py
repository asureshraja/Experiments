from django.http import HttpResponse
from django.template import Context, loader
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import random, string,time
msg=""
i=0
finaltime=0

def index(request):
    msg="welcome"
    template = loader.get_template('templates/story/test.html')
    context = Context({
        'msg': msg,
    })    
    return HttpResponse(template.render(context))

def ttime(request):
    global i
    if(open(str(msg+"time"),"r+").read()==""):
        return HttpResponse("yet to start!!!")
    finaltime=int(open(str(msg+"time"),"r+").read())
    f=open(msg+"active","r+")
    m=f.read()
    f.close()
    mems=m.split("=")
    if(finaltime<time.time()):
        cf=open(msg+"curactive","w+")
        cf.write("123failed")
        cf.close()
        return HttpResponse("Game over!")
    i=(int(((finaltime-time.time()) / 15))%(len(mems)-1)) +1
    cf=open(msg+"curactive","w+")
    cf.write(mems[i])
    cf.close()
    return HttpResponse(open(msg+"curactive","r+").read())


def starter(request):
    if(open(str(msg+"time"),"r+").read()==""):
        fo = open(str(msg+"time"), "w")
        fo.write(str((int(time.time())+180)))
        fo.close()
    return HttpResponse(open(str(msg+"time"),"r+").read())

def fullstory(request):
    global msg
    fname=msg
    if(fname==""):
        return HttpResponse("BAD REQUEST CONTACT ADMIN")
    h=open(fname,'r+')
    content=h.read();
    h.close()
    return HttpResponse(content)


@csrf_exempt
def chkuser(request):
    f=open(msg+"active","r+")
    m=f.read()
    f.close()
    mems=m.split("=")
    for e in mems:
        if e==request.GET['nick']:
            return HttpResponse("0")
    return HttpResponse("1")


@csrf_exempt
def addstory(request):
    global msg
    nick=request.POST['nick']
    if nick==open(msg+"curactive").read() :
        fname=msg
        
        f=open(fname,'a+')
        f.write(request.POST['sentence'])
        f.close()
        
        f=open(str(fname+"meta"),'a+')
        f.write("["+request.POST['sentence']+"--by->"+nick+"]")
        f.close()
    else:
        return HttpResponse("its not your turn....!")
    return HttpResponse(open(str(fname+"meta")).read())

def viewstory(request):
    a=open(str(msg+"meta")).read()

    return HttpResponse(a)






@csrf_exempt
def adduser(request):
    f=open(msg+"active","a+")
    f.write("="+request.POST['nick'])
    f.close()
    return HttpResponse("1")



def randomword(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))


def tuser(request):
    wel="welcome"
    template = loader.get_template('templates/story/index.html')
    context = Context({
        'wel': wel,
    })
    return HttpResponse(template.render(context))

def tadmin(request):
    template = loader.get_template('templates/story/admin.html')
    context = Context({
        'msg': msg,
    })
    return HttpResponse(template.render(context))




def prework(request):
    global msg,finaltime
    finaltime=time.time()+180
    msg=randomword(3)
    fo = open(msg, "w")
    fo.write(" ")
    fo.close()
    fo = open(str(msg+"meta"), "w")
    fo.write("")
    fo.close()
    fo = open(str(msg+"active"), "w")
    fo.write("")
    fo.close()
    fo = open(str(msg+"curactive"), "w")
    fo.write("")
    fo.close()
    fo = open(str(msg+"time"), "w")
    fo.write("")
    fo.close()
    return HttpResponse(msg)
