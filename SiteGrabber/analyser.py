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
    response = br.open("https://www.google.co.in/search?q=oracle+java")
    page=response.read()
except httplib.IncompleteRead, e:
    page  = e.partial

print response
parser.feed(page)

print "total data extracted",len(parser.parsedop)

while(True):
    searchkey=raw_input("enter phrase to search component number")
    i=0
    for p in parser.parsedop:
        p=p[2]
        if(unicode(p, errors='ignore').find(searchkey)>=0):
            print "found in",i,"component"

        i=i+1
    temp=raw_input("do you want to search again?0 to NO and 1 to Yes")
    if(int(temp)==0):
        break

while(True):
    inp=raw_input("enter val < max and 0 for exit")
    inp=int(inp)
    if(inp==0):
        break
    print parser.parsedop[inp][2]


