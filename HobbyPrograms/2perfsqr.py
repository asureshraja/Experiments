num=int(raw_input("enter a number "))
i=1
j=3
while (i<num):
	print i," ",num
	i=i+j
	j=j+2

if(i==num):
	print "perfect square"
else:
	print "not perfect square"