dit={'q':1,'w':2,'e':3,'r':4,'t':5,'y':6,'u':7,'i':8,'o':9,'p':10,'a':11,'s':12,'d':13,'f':14,'g':15,'h':16,'j':17,'k':18,'l':19,'z':20,'x':21,'c':22,'v':23,'b':24,'n':25,'m':26}
rdit={}
def initiate():
	global rdit
	for keys,values in dit.iteritems():
		rdit[values]=keys

def generate(s):
	global dit
	a=[0]*390
	for i in range(0,len(s)):
		a[i*26+dit[s[i]]-1]=1
	return a

def reverse(a):
	initiate()
	global rdit
	s=[i for i,x in enumerate(a) if x == 1]
	final=""
	for n in s:
		final=final+str(rdit[(n%26)+1])
	return final
