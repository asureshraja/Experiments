dit={'q':1,'w':2,'e':3,'r':4,'t':5,'y':6,'u':7,'i':8,'o':9,'p':10,'a':11,'s':12,'d':13,'f':14,'g':15,'h':16,'j':17,'k':18,'l':19,'z':20,'x':21,'c':22,'v':23,'b':24,'n':25,'m':26}
rdit={}
def initiate():
	global rdit
	for keys,values in dit.iteritems():
		rdit[values]=keys
def generate(s):
	global dit
	a=[0]*10
	for i in range(0,len(s)):
		t= float(float(dit[s[i]])/26)
		a[i]=t
	return a

def reverse(a,j=1):
	global dit
	s=[0]*10
	for i in range(0,j):
		if(a[i]==0):
			break
		s[i]=rdit[int(a[i]*26)]
	return ''.join(str(e) for e in s if e != 0)
