import urllib
from HTMLParser import HTMLParser
FILENAME="girl"
start = "Indian baby names or hindu girl names with letter A"
stop="Ad-Al"
flag=0
class newParser(HTMLParser):
	def handle_data(self, data):
		global start,stop,flag
		if (data.strip()==start):
			flag=1
			return
		if (data.strip()==stop):
			flag=0
		if (flag==1):
			print data.strip().split("=")[0].strip()
			#f = open(FILENAME,'a+')
			#f.write(data.strip()+",")
			#f.close()

url = "http://www.indianhindunames.com/indian-hindu-girl-name-a.htm"
page = urllib.urlopen(url).read()
parser = newParser()
parser.feed(page)