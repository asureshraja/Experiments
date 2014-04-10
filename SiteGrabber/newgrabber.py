from HTMLParser import HTMLParser
import urllib2
import mechanize
class grabber(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.parsedop=[]
        self.tag = None
        self.attribs=None
        self.template=""

    def handle_starttag(self, tag, attrs):
        if(tag.upper()=="HTML"):
            self.template=self.template+"HTML "
        if(tag.upper()=="HEAD"):
            self.template=self.template+"HEAD "
        if(tag.upper()=="DIV"):
            self.template=self.template+"DIV "
        if(tag.upper()=="TABLE"):
            self.template=self.template+"TABLE "
        if(tag.upper()=="SPAN"):
            self.template=self.template+"SPAN "
        self.tag=tag
        self.attribs=attrs


    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        if(len(data.strip())!=0 and data.find("{")<0):
            temp=self.attribs
            if(temp==None or temp==[]):
                temp=self.tag
            self.parsedop.append([self.tag,temp,data.strip(),self.template])



parser = grabber()
try:
    br = mechanize.Browser()
    br.set_handle_robots(False)   # ignore robots
    br.set_handle_refresh(False)  # can sometimes hang without this
    br.addheaders = [('User-agent', 'Firefox')]
    response = br.open("https://www.google.co.in/search?q=visualisation+in+r+for+tweets")
    page=response.read()
except httplib.IncompleteRead, e:
    print "error"
    page  = e.partial
parser.feed(page)

frmto=raw_input("enter component numbers from and to example(34 39) for extraction")
frm=int(frmto.split(" ")[0])
to=int(frmto.split(" ")[1])

f = open("urls.txt")
lines = f.readlines()
f.close()


#beforepattern=int(raw_input("enter component number of pattern before data"))
beforepattern=frm-1
#afterpattern=int(raw_input("enter component number of pattern after data"))
afterpattern=to+1
verbose=int(raw_input("enter verbose mode?0/1"))
if(verbose==1):
    i=0
    for p in parser.parsedop:
        p=p[3]
        if(p==parser.parsedop[beforepattern][3]):
            print "data found" , parser.parsedop[beforepattern][2]
            beforepattern=i
            if(int(raw_input("do you want to continue with data 1 for Yes and 0 for No"+str(unicode(parser.parsedop[beforepattern][2], errors='ignore'))))==1):
                break
        i=i+1

    i=0
    print "one finished"
    for p in parser.parsedop:
        p=p[3]
        if(p==parser.parsedop[afterpattern][3]):
            print "data found" , parser.parsedop[afterpattern][2]
            afterpattern=i
            if(int(raw_input("do you want to continue with data 1 for Yes and 0 for No"+str(unicode(parser.parsedop[afterpattern][2], errors='ignore'))))==1):
                break
        i=i+1


print beforepattern,afterpattern

finaloutput=[]
output=""
for i in range(beforepattern,afterpattern):
    p=parser.parsedop[i][2]
    output=output+p

finaloutput.append(output)
for line in lines:
    print line
    output=""

    newbfr=0
    newaftr=0
    newparser = grabber()
    try:
        br = mechanize.Browser()
        br.set_handle_robots(False)   # ignore robots
        br.set_handle_refresh(False)  # can sometimes hang without this
        br.addheaders = [('User-agent', 'Firefox')]
        response = br.open(line)
        page=response.read()
    except httplib.IncompleteRead, e:
        print "error"
        page  = e.partial

    newparser.feed(page)
    print len(newparser.parsedop)
    i=0
    while(True):
        if(i>=len(newparser.parsedop)):
            print newparser.parsedop[i-1][3]
            print ("failed")
            break
        print len(newparser.parsedop[i][3]),len(parser.parsedop[beforepattern][3])
        if(len(newparser.parsedop[i][3])==len(parser.parsedop[beforepattern][3])):
            newbfr=i
            break
        i=i+1

    i=0
    while(True):
        if(i>=len(newparser.parsedop)):
            print newparser.parsedop[i-1][3]
            print ("failed")
            break
        while(len(newparser.parsedop[i][3])==len(parser.parsedop[afterpattern][3])):
            newaftr=i
            break
        i=i+1

    print newbfr,newaftr
    for i in range(newbfr,newaftr):
        print p
        p=newparser.parsedop[i][2]
        output=output+p
    finaloutput.append(output)

print finaloutput